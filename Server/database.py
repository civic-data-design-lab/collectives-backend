import pymongo
from Server import settings as ss
from bson.json_util import dumps

# Connect to mongodb test database
client = pymongo.MongoClient(host=ss.DATABASE_ADDRESS, port=ss.DATABASE_PORT)
db = client.test


def add_item(name, age, course, dorm):
    '''
    Adds the item to the database
    :param name:
    :param age:
    :param course:
    :param dorm:
    :return: ID of added item
    '''
    students = db.student
    student = {"name": name, "age": age, "course": course, "dorm": dorm}
    student_id = students.insert_one(student).inserted_id
    return student_id


def get_items():
    '''
    :return: List of all the items in student collection in database
    '''
    followers = db.collectives
    result = []
    for follower in followers.find():
        result.append(follower['follower'])
    return dumps(result)


def get_collection (collection):
    '''
    :return: Returns the mongodb collection for access
    '''
    return db[collection].find()

def get_followers():
    '''
    :return: List of all the items in student collection in database
    '''
    print('getting previous followers')
    followers = db.collectives
    result = {}
    for follower in followers.find():
        if len(follower['tweets']) != 0:
            result[follower['follower']] = follower['tweets'][0]['id']
    return result


def add_raw_tweet(follower, tweets):
    collectives = db.collectives
    row = {"follower": follower, "tweets": tweets}
    row_id = collectives.insert_one(row).inserted_id
    return row_id


def append_raw_tweet(follower, tweets):
    collectives = db.collectives
    collectives.update_one(
        {'follower': follower},
        {'$push': {'tweets': {'$each': tweets}}}
    )
    return


def drop_collection(collection):
    db[collection].drop()
