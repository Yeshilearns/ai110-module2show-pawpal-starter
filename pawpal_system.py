from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    duration: int
    priority: int
    category: Optional[str] = None
    completed: bool = False
    time: Optional[str] = None
    pet_name: Optional[str] = None
    frequency: Optional[str] = None   # "daily" or "weekly"
    due_date: Optional[date] = None

    def mark_complete(self) -> Optional["Task"]:
        """Mark this task as completed and create the next recurring task if needed."""
        self.completed = True

        if self.frequency == "daily":
            next_date = (self.due_date or date.today()) + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = (self.due_date or date.today()) + timedelta(days=7)
        else:
            return None

        return Task(
            title=self.title,
            duration=self.duration,
            priority=self.priority,
            category=self.category,
            completed=False,
            time=self.time,
            pet_name=self.pet_name,
            frequency=self.frequency,
            due_date=next_date,
        )

    def update_task(
        self,
        title: Optional[str] = None,
        duration: Optional[int] = None,
        priority: Optional[int] = None,
        category: Optional[str] = None,
        time: Optional[str] = None,
    ) -> None:
        """Update task fields if new values are provided."""
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if priority is not None:
            self.priority = priority
        if category is not None:
            self.category = category
        if time is not None:
            self.time = time


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        task.pet_name = self.name
        self.tasks.append(task)

    def remove_task(self, task_title: str) -> None:
        """Remove a task by its title."""
        for i, task in enumerate(self.tasks):
            if task.title == task_title:
                del self.tasks[i]
                return

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: List[str] = field(default_factory=list)
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name."""
        for i, pet in enumerate(self.pets):
            if pet.name == pet_name:
                del self.pets[i]
                return

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self) -> None:
        """Initialize the scheduler."""
        self.last_plan: List[Task] = []

    def generate_schedule(self, owner: Owner) -> List[Task]:
        """Generate a schedule based on priority and available time."""
        all_tasks = owner.get_all_tasks()
        pending = [task for task in all_tasks if not task.completed]
        sorted_tasks = self.sort_tasks(pending)

        scheduled: List[Task] = []
        remaining = owner.available_time

        for task in sorted_tasks:
            if task.duration <= remaining:
                scheduled.append(task)
                remaining -= task.duration

        self.last_plan = scheduled
        return scheduled

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by priority and duration."""
        return sorted(tasks, key=lambda task: (-task.priority, task.duration))

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time in HH:MM format."""
        return sorted(
            tasks,
            key=lambda task: task.time if task.time is not None else "23:59",
        )

    def filter_tasks(
        self,
        tasks: List[Task],
        completed: Optional[bool] = None,
        pet_name: Optional[str] = None,
    ) -> List[Task]:
        """Filter tasks by completion status or pet name."""
        filtered = tasks

        if completed is not None:
            filtered = [task for task in filtered if task.completed == completed]

        if pet_name is not None:
            filtered = [task for task in filtered if task.pet_name == pet_name]

        return filtered

    def explain_plan(self) -> str:
        """Explain how the schedule was created."""
        if not self.last_plan:
            return "No plan generated yet."

        total = sum(task.duration for task in self.last_plan)
        count = len(self.last_plan)

        return (
            f"Scheduled {count} tasks totaling {total} minutes. "
            "Higher-priority tasks were chosen first while staying within the available time."
        )