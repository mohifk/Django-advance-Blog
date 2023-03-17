from celery import shared_task
from time import sleep

@shared_task
def SendEmail()
    sleep(3)
    print('done send email')