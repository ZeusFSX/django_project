import random

from celery import shared_task, Task


class CallbackTask(Task):
    def run(self, *args, **kwargs):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        print("TaskID=%s, Result is %s" % (task_id, retval))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass


@shared_task(name="sum_two_numbers", base=CallbackTask)
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers", base=CallbackTask)
def mul(x, y):
    total = x * y
    return total
