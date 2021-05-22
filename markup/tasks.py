from time import sleep
from celery import shared_task, Task


class CallbackTask(Task):
    def run(self, *args, **kwargs):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        print("TaskID=%s, Result is %s" % (task_id, retval))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass


@shared_task(name="send_email_tasks", base=CallbackTask)
def send_email(emails: list):
    return emails


@shared_task(name="some_long_work", base=CallbackTask)
def long_work(time):
    sleep(time)

