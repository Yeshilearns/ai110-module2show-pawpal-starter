from pawpal_system import Task, Pet


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