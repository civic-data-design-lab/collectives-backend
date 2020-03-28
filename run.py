import sys
import os
CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
sys.path.append(CURRENT_DIR)
sys.path.append(CURRENT_DIR+'/services/')
sys.path.append(CURRENT_DIR+'/Server/')

from Server import app
import Server.views
from Server.logger import logger
from Server.settings import SERVER_HOST, SERVER_PORT
import Server.settings as ss
from apscheduler.schedulers.background import BackgroundScheduler
from Server.job import JOB
from datetime import datetime

logger.info("Start Server")

# start scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(JOB, ss.SCHEDULER_MODE, seconds=ss.SCHEDULER_INTERVAL, next_run_time=datetime.now())
scheduler.start()


# start flask service
if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True, threaded=True, use_reloader=False)


