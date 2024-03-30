def leastInterval(tasks,n):
    tasks.sort()
    # Count number of occurnces
    letter_counts = {task: tasks.count(task) for task in tasks}
    cooling_time = n
    