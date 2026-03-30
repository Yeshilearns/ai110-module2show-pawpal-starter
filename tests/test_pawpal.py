from datetime import date, timedelta
from pawpal_system import Task, Pet, Scheduler


def test_mark_complete():
    task = Task(title="Feed", duration=10, priority=5)
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet(name="Buddy", species="Dog", age=3)
    task = Task(title="Walk", duration=20, priority=4)

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Walk"
    assert pet.tasks[0].pet_name == "Buddy"


def test_sort_by_time_returns_tasks_in_chronological_order():
    scheduler = Scheduler()

    task1 = Task(title="Vet Visit", duration=60, priority=4, time="11:00")
    task2 = Task(title="Feed Pet", duration=10, priority=5, time="08:00")
    task3 = Task(title="Morning Walk", duration=30, priority=3, time="09:00")

    tasks = [task1, task2, task3]
    sorted_tasks = scheduler.sort_by_time(tasks)

    assert [task.title for task in sorted_tasks] == [
        "Feed Pet",
        "Morning Walk",
        "Vet Visit",
    ]


def test_daily_recurring_task_creates_next_day_task():
    today = date.today()
    task = Task(
        title="Feed Pet",
        duration=10,
        priority=5,
        time="08:00",
        frequency="daily",
        due_date=today,
    )

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.title == "Feed Pet"
    assert next_task.frequency == "daily"
    assert next_task.due_date == today + timedelta(days=1)
    assert next_task.completed is False


def test_detect_conflicts_flags_duplicate_times():
    scheduler = Scheduler()

    task1 = Task(title="Morning Walk", duration=30, priority=3, time="09:00")
    task2 = Task(title="Grooming", duration=25, priority=3, time="09:00")
    task3 = Task(title="Feed Pet", duration=10, priority=5, time="08:00")

    warnings = scheduler.detect_conflicts([task1, task2, task3])

    assert len(warnings) == 1
    assert "Conflict detected" in warnings[0]
    assert "09:00" in warnings[0]