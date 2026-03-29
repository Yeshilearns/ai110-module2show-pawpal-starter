from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner and pets
owner = Owner(name="Alex", available_time=120)

pet1 = Pet(name="Buddy", species="Dog", age=3)
pet2 = Pet(name="Whiskers", species="Cat", age=2)

owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks out of order by time
task1 = Task(
    title="Vet Visit",
    duration=60,
    priority=4,
    time="11:00",
    due_date=date.today()
)

task2 = Task(
    title="Feed Pet",
    duration=10,
    priority=5,
    time="08:00",
    frequency="daily",
    due_date=date.today()
)

task3 = Task(
    title="Morning Walk",
    duration=30,
    priority=3,
    time="09:00",
    frequency="weekly",
    due_date=date.today()
)

task4 = Task(
    title="Play Time",
    duration=20,
    priority=2,
    time="07:30",
    due_date=date.today()
)

task5 = Task(
    title="Grooming",
    duration=25,
    priority=3,
    time="09:00",
    due_date=date.today()
)

# Mark one task as completed for filtering test
task4.mark_complete()

# Assign tasks to pets
pet1.add_task(task1)
pet1.add_task(task3)

pet2.add_task(task2)
pet2.add_task(task4)
pet2.add_task(task5)

# Create scheduler
scheduler = Scheduler()

# Original tasks
all_tasks = owner.get_all_tasks()

print("Original Task Order:")
for task in all_tasks:
    print(
        f"- {task.title} | pet={task.pet_name} | time={task.time} | completed={task.completed}"
    )

# Sort by time
sorted_by_time = scheduler.sort_by_time(all_tasks)

print("\nTasks Sorted by Time:")
for task in sorted_by_time:
    print(f"- {task.title} ({task.time})")

# Filter incomplete tasks
incomplete_tasks = scheduler.filter_tasks(all_tasks, completed=False)

print("\nIncomplete Tasks:")
for task in incomplete_tasks:
    print(f"- {task.title} | completed={task.completed}")

# Filter by pet name
buddy_tasks = scheduler.filter_tasks(all_tasks, pet_name="Buddy")

print("\nTasks for Buddy:")
for task in buddy_tasks:
    print(f"- {task.title} | pet={task.pet_name}")

# Detect conflicts
conflicts = scheduler.detect_conflicts(all_tasks)

print("\nConflict Check:")
if conflicts:
    for warning in conflicts:
        print(f"- {warning}")
else:
    print("No conflicts detected.")

# Generate schedule
schedule = scheduler.generate_schedule(owner)

print("\nToday's Schedule:")
for task in schedule:
    print(
        f"- {task.title} ({task.duration} mins, priority {task.priority}, time {task.time})"
    )

print("\nExplanation:")
print(scheduler.explain_plan())

# Test recurring tasks
print("\nRecurring Task Test:")
next_feed_task = task2.mark_complete()
print(f"Completed current task: {task2.title} | completed={task2.completed}")

if next_feed_task:
    print(
        f"Next recurring task created: {next_feed_task.title} | "
        f"frequency={next_feed_task.frequency} | due_date={next_feed_task.due_date}"
    )

next_walk_task = task3.mark_complete()
print(f"Completed current task: {task3.title} | completed={task3.completed}")

if next_walk_task:
    print(
        f"Next recurring task created: {next_walk_task.title} | "
        f"frequency={next_walk_task.frequency} | due_date={next_walk_task.due_date}"
    )