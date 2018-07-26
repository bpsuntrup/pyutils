''' prioritizer.py
takes a list of tasks and aids in prioritization of tasks. '''
import itertools
from bite import bite

# Please make this even for now
tasks = [
    'write story',
    'learn to cook',
    'do dishes',
    'feed poor people',
    'go on an adventure',
    'invest money',
    'learn a new language',
    'apply for a job',
    'teach my child something new',
    'talk to my wife',
    'develop an app',
]

tasks = { task: 0 for task in tasks}

def best(tasks):
    """ tasks must be a dict of tasks and non-negative integers """
    best_score = 0
    bests = {}
    for task, val in tasks.items():
        if val > best_score:
            bests = {
                task: val,
            }
            best_score = val
        elif val == best_score:
            bests[task] = val
    return bests

dangling_task = None



while len(best(tasks).items()) > 1:
    i = iter(best(tasks))
    if dangling_task is not None:
        i = itertools.chain(i, [dangling_task,])
        dangling_task = None
    for task1, task2 in bite(i):
        if task2 is None:
            dangling_task = task1
            break

        # Now get user input
        print('1. {}'.format(task1))
        print('2. {}'.format(task2))
        print('3. Quit and exit.')
        while True:
            try:
                answer = int(input())
                if answer not in [1,2,3]:
                    raise ValueError
                break
            except ValueError:
                print('Input must be 1, 2, or 3.')
        if answer == 1:
            print('you chose: {}'.format(task1))
            tasks[task1] = max(tasks[task2] + 1, tasks[task1])
        elif answer == 2:
            print('you chose: {}'.format(task2))
            tasks[task2] = max(tasks[task1] + 1, tasks[task2])
        else:
            print best((tasks))
            exit(0)

best_task = best(tasks)
print ( 'Results: {}'.format(best_task))
print ('You should \"{}\"'.format(best_task.keys()[0]))
