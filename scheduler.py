# File: scheduler.py
# Author: @StupidZY

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def run_tasks(self):
        for task in self.tasks:
            if task.should_run():
                task.run()


class ScheduledTask:
    def __init__(self, device, action, condition):
        self.device = device
        self.action = action
        self.condition = condition

    def should_run(self):
        return self.condition()

    def run(self):
        self.action()
