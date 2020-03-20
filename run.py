from Server import app
import Server.views
from Server.logger import logger
from Server.settings import SERVER_HOST, SERVER_PORT
import Server.settings as ss
from apscheduler.schedulers.background import BackgroundScheduler
from Server.job import JOB
from datetime import datetime
import sys
sys.path.append('services/')
sys.path.append('Server/')

logger.info("Start Server")


# start scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(JOB, ss.SCHEDULER_MODE, seconds=ss.SCHEDULER_INTERVAL, next_run_time=datetime.now())
scheduler.start()


# start flask service
if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True, threaded=True, use_reloader=False)


