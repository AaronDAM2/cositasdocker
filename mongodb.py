# mongodb.py
import pymongo

def insert_data(collection):
    data = [
        {"name": "John", "age": 25},
        {"name": "Jane", "age": 30},
        {"name": "Jim", "age": 35},
        {"name": "Joan", "age": 40},
    ]
    collection.insert_many(data)

def update_data(collection):
    collection.update_one({"name": "John"}, {"$set": {"age": 28}})

def delete_data(collection):
    collection.delete_one({"name": "Jane"})

def destroy_data(collection):
    collection.drop()

def main():
    client = pymongo.MongoClient("mongodb://admin:adminpass@localhost:27017/")
    db = client["test_db"]
    collection = db["test_collection"]

    insert_data(collection)
    update_data(collection)
    delete_data(collection)
    destroy_data(collection)

    client.close()

if __name__ == "__main__":
    main()
