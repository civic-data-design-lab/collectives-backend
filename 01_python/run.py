from Server import app
import Server.views
from Server.logger import logger
from Server.settings import SERVER_HOST, SERVER_PORT
import Server.settings as ss
from apscheduler.schedulers.background import BackgroundScheduler
from Server.job import JOB
from Server.database import MongoDB_Demo

logger.info("Start Server")

# start scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(JOB, ss.SCHEDULER_MODE, seconds=ss.SCHEDULER_INTERVAL)
scheduler.start()

# First time to run the job
JOB()

# Database demo
MongoDB_Demo()

# start flask service
app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False, threaded=True)