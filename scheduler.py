from apscheduler.schedulers.blocking import BlockingScheduler
from strategy import run_once

sched = BlockingScheduler(timezone="UTC")
sched.add_job(run_once, "cron", second=5)   # HH:MM:05 every minute
sched.start()
