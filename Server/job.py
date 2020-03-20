from Server import database
import random
import sys
# Add parent directory to system path to be able to resolve Server folder
sys.path.append('../')
from services import twitter

def JOB():
    """
    A demo for scheduler
    :return:
    """
    print("Running the job")
    twitter.get_new_tweets()  # Comment this line to be able ot use the api
    # database.add_item("John Doe", random.randint(10, 60), random.randint(1, 23), "Maseeh")
    return
