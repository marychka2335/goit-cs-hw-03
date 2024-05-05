import logging
from psycopg2 import DatabaseError
from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from create_document import create_documents

#Get data from .env file. You need to create env file with data in .env-example
config = dotenv_values('.env')
url = f"mongodb+srv://{config['USER_MG']}:{config['PASS_MG']}@cluster0.jw3kqfo.mongodb.net/?retryWrites=true&w=majority&appName=Clustero"

client = MongoClient(url, server_api = ServerApi('1'))
db = client['cats_database']
cats_collection = db['cats']

def create_cat():
    name = input("Please enter name - ")
    age = input("Please enter age - ")
    
    features = []
    while True:
        entered = input("Please enter feature (or 'exit' to finish) - ")
        if entered.lower() in ['exit', 'q']:
            break
        features.append(entered)
    
    cats_collection.insert_one({"name": name, "age": age, "features": features})
    print(f"Next cat was added name:'{name}', age: '{age}', features: '{features}' .")

def read_all_cats():
    all_cats = cats_collection.find()
    for cat in all_cats:
        print(cat)

def find_cat_by_name():
    name = input("Please enter name - ")
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat with the name '{name}' not found.")

def update_cat_age():
    name = input("Please enter name - ")
    new_age = input("Please enter new age - ")
    cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"Age of the cat named '{name}' updated to {new_age} years.")

def update_cat_name():
    name = input("Please enter name - ")
    new_name = input("Please enter NEW name - ")
    cats_collection.update_one({"name": name}, {"$set": {"name": new_name}})
    print(f"Name of the cat named '{name}' updated to '{new_name}'.")

def add_cat_feature():
    name = input("Please enter name - ")
    new_feature = input("Please enter new feature - ")
    cats_collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print(f"New feature '{new_feature}' added to the cat named '{name}'.")

def delete_cat_by_name():
    name = input("Please enter name - ")
    result = cats_collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Cat with the name '{name}' successfully deleted.")
    else:
        print(f"Cat with the name '{name}' not found.")

def delete_all_cats():
    result = cats_collection.delete_many({ })
    print(f"Deleted {result.deleted_count} cats.")

if __name__ == '__main__':
    try:
        while True:
            action = input("""Please enter action: 
    1. To to create cats db 'cdb'
    2. To create new cat - 'ccat'
    3. To read all cats - 'r'
    4. To read by name - 'rn'
    5. To update age - 'ua'
    6. To update cat`s name - 'un'
    7. To add cat`s feature - 'uf'
    8. To delete cat by name - 'dn'
    9. To delete all cats - 'dall'
    """)
            match action.lower():
                case 'cdb':
                    #Use it before another action
                    create_documents(cats_collection)
                case 'ccat':
                    create_cat()
                case 'r':
                    read_all_cats()
                case 'rn':
                    find_cat_by_name()
                case 'ua':
                    update_cat_age()
                case 'un':
                    update_cat_name()
                case 'uf':
                    add_cat_feature()
                case 'dn':
                    delete_cat_by_name()
                case 'dall':
                    delete_all_cats()
            entered = input("If you want to exit enter q or exit - ")
            if entered.lower() in ['exit', 'q']:
                break

    except Exception as e:
        print(e)