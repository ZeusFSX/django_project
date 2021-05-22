from time import sleep
from celery import shared_task, Task
from django.core.mail import EmailMessage
from markup.models import Entity


class CallbackTask(Task):
    def run(self, *args, **kwargs):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        print("TaskID=%s, Result is %s" % (task_id, retval))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass


@shared_task(name="send_email_tasks")
def send_email(emails: list):
    message_content = "hello from celery and django"
    msg = EmailMessage("hello", message_content, 'zeusfsxtmp@gmail.com', emails)
    msg.send()
    return "successful"


@shared_task(name="some_long_work", base=CallbackTask)
def long_work(time):
    sleep(time)
    count_entity = Entity.objects.count()
    return count_entity

