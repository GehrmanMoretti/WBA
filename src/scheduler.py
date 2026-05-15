from apscheduler.schedulers.background import BackgroundScheduler
from weibo_api import WeiboAPI
import os

def post_daily_update():
    token = os.getenv("WEIBO_ACCESS_TOKEN")
    api = WeiboAPI(token)
    api.post_status("自动化测试消息")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_daily_update, 'cron', hour=9)
    scheduler.start()
    print("Scheduler started.")