import pymongo
from pymongo import MongoClient


def test():

    client = MongoClient("192.168.233.141",27017)
    db = client["taiwan"]
    collection = db["hanjianbing"]
    for row in collection:
        print(row.values())


# client = pymongo.MongoClient("192.168.233.141",27017)
# db = client.test
# collection = db.test
# collection.insert({"name":'Tom',"age":25,"addr":'Cleveland'})


def get_db_collection(db, collection):
    client = MongoClient(cp.get("mongodb", "host"), 27017)
    current_db = client[db]
    current_collection = current_db[collection]

    # current_db.authenticate("admin", "ga2016")
    return current_collection

if __name__ == '__main__':
    test()