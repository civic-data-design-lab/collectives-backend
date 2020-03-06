import pymongo
from Server import settings as ss

def MongoDB_Demo():
    """
    Demo of using mongoDB
    :return:
    """

    # Connect to mongodb
    client = pymongo.MongoClient(host = ss.DATABASE_ADDRESS, port = ss.DATABASE_PORT)
    db = client.demodata

    db_demo = db.demo
    db_demo.test.create_index("id")

    id_to_search = 1
    if db_demo.find_one({"id":id_to_search}):
        print("ID existed")
    else:
        data = {
            "id":id_to_search
        }
        db_demo.insert_one(data)
        print("ID inserted")
        pass
    pass