import logging
from random import randint, choice
from faker import Faker
from psycopg2 import DatabaseError
from connection import connect

fake_data = Faker('en_US')
COUNT = 1_000

#create COUNT times query to add status
def insert_status(crs, cnct):
    statuses = ['new', 'in progress', 'completed']
    try:
        for _ in range(COUNT):
            status_name = choice(statuses)
            crs.execute((f"INSERT INTO status (name) VALUES ('{status_name}');"))
        cnct.commit()
    except DatabaseError as e:
        logging.error(e)
        cnct.rollback()

    
#create COUNT times query to add users
def insert_users(crs, cnct):
    try:
        for _ in range(COUNT):
            fullname = fake_data.name()
            email = fake_data.email()
            while True:
                crs.execute("SELECT EXISTS(SELECT 1 FROM users WHERE email = %s);", (email,))
                exists = crs.fetchone()[0]
                if not exists:
                    break
                email = fake_data.email()
            crs.execute(f"INSERT INTO users (fullname, email) SELECT '{fullname}', '{email}' WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = '{email}');")

        cnct.commit()
    except DatabaseError as e:
        logging.error(e)
        cnct.rollback()
        
#create COUNT times query to add tasks
def insert_tasks(crs, cnct):
    try:
        for _ in range(COUNT):
            title = fake_data.sentence()
            description = fake_data.paragraph()
            user_id = randint(1, COUNT)
            status_id = randint(1, COUNT)
            
            while True:
                crs.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id = %s);", (user_id,))
                exists = crs.fetchone()[0]
                if exists:
                    break
                user_id = randint(1, COUNT)
                status_id = randint(1, COUNT)
                
            crs.execute("INSERT INTO tasks (title, description, user_id, status_id) VALUES (%s, %s, %s, %s);", (title, description, user_id, status_id))

        cnct.commit()
    except DatabaseError as e:
        logging.error(e)
        cnct.rollback()