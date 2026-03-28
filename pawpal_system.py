from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
	title: str
	duration: int
	priority: int
	category: Optional[str] = None
	completed: bool = False

	def mark_complete(self) -> None:
		self.completed = True

	def update_task(self, title=None, duration=None, priority=None, category=None) -> None:
		if title is not None:
			self.title = title
		if duration is not None:
			self.duration = duration
		if priority is not None:
			self.priority = priority
		if category is not None:
			self.category = category


@dataclass
class Pet:
	name: str
	species: str
	age: int
	tasks: List[Task] = field(default_factory=list)

	def add_task(self, task: Task) -> None:
		"""Add a Task to this pet's task list."""
		self.tasks.append(task)

	def remove_task(self, task_title: str) -> None:
		"""Remove the first Task with matching title."""
		for i, t in enumerate(self.tasks):
			if t.title == task_title:
				del self.tasks[i]
				return

	def get_tasks(self) -> List[Task]:
		"""Return this pet's list of tasks."""
		return self.tasks


@dataclass
class Owner:
	name: str
	available_time: int
	preferences: List[str] = field(default_factory=list)
	pets: List[Pet] = field(default_factory=list)

	def add_pet(self, pet: Pet) -> None:
		self.pets.append(pet)

	def remove_pet(self, pet_name: str) -> None:
		for i, pet in enumerate(self.pets):
			if pet.name == pet_name:
				del self.pets[i]
				return

	def get_all_tasks(self) -> List[Task]:
		all_tasks = []
		for pet in self.pets:
			all_tasks.extend(pet.get_tasks())
		return all_tasks


class Scheduler:
	def __init__(self) -> None:
		self.last_plan: List[Task] = []

	def generate_schedule(self, owner: Owner) -> List[Task]:
		"""Generate a simple daily schedule for the owner."""
		all_tasks = owner.get_all_tasks()
		pending = [t for t in all_tasks if not t.completed]
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
		"""Return tasks sorted by priority (higher number = higher priority)."""
		return sorted(tasks, key=lambda t: (-t.priority, t.duration))

	def explain_plan(self) -> str:
		"""Return a short explanation of the last generated plan."""
		if not self.last_plan:
			return "No plan generated yet."

		total = sum(task.duration for task in self.last_plan)
		count = len(self.last_plan)
		return f"Scheduled {count} tasks totaling {total} minutes. Higher-priority tasks were chosen first, while staying within the owner's available time."

