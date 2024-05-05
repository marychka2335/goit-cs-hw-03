import logging
from psycopg2 import DatabaseError
from connection import connect
from insert_generation import insert_users,insert_status,insert_tasks

#Read sql file and do query
def sql_create(cnct, sqt_file: str):
    crs = cnct.cursor()
    try:
        with open(sqt_file, 'r') as f:
            sql_statements = f.read()
        crs.execute(sql_statements)
        cnct.commit()
    except DatabaseError as e:
        logging.error(e)
        cnct.rollback()
    
#Do three guery to create tables - users, status and tasks
def sql_insert(cnct):
    crs = cnct.cursor()
    try:
        insert_users(crs, cnct)
        insert_status(crs, cnct)
        insert_tasks(crs, cnct)
    finally:
        crs.close()

        
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sql_file_path = "create_tables.sql"

    with connect() as cnct:
        try:
            with cnct.cursor() as crs:
                sql_create(cnct, sql_file_path)
                sql_insert(cnct)
        except DatabaseError as e:
            logging.error(e)