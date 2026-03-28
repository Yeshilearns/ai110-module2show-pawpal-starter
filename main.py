from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner and pets
owner = Owner(name="Alex", available_time=120)

pet1 = Pet(name="Buddy", species="Dog", age=3)
pet2 = Pet(name="Whiskers", species="Cat", age=2)

owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks
task1 = Task(title="Morning Walk", duration=30, priority=3)
task2 = Task(title="Feed Pet", duration=10, priority=5)
task3 = Task(title="Vet Visit", duration=60, priority=4)

# Assign tasks
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)

# Generate schedule
scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)

# Print results
print("Today's Schedule:")
for task in schedule:
    print(f"- {task.title} ({task.duration} mins, priority {task.priority})")

print("\nExplanation:")
print(scheduler.explain_plan())