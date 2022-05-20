from apscheduler.schedulers.background import BackgroundScheduler
from updateservice import update

def start():
    scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 2})
    scheduler.add_job(update.get_data,'interval', minutes=60)
    scheduler.start()
