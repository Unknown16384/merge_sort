from datetime import datetime
class Tasks:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)
    def run(self):
        if len(self.tasks) > 0:
            self.tasks[0]()
            print(f'{datetime.now()} задача {self.tasks[0].__name__} завершена')
            self.tasks.pop(0)
            return self.run()
        else:
            print('все задачи завершены')

def task1():
    '''пример задачи 1'''
    a = 10000000
    while a > 0:
        a -= 1
def task2():
    '''пример задачи 2'''
    a = 100000000
    while a > 0:
        a -= 1
tasks = Tasks()
tasks.add(task1)
tasks.add(task2)
tasks.run()