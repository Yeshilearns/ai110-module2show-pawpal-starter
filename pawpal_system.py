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
		pass

	def update_task(self) -> None:
		pass


@dataclass
class Pet:
	name: str
	species: str
	age: int
	tasks: List[Task] = field(default_factory=list)

	def add_task(self, task: Task) -> None:
		pass

	def remove_task(self, task_title: str) -> None:
		pass

	def get_tasks(self) -> List[Task]:
		pass


@dataclass
class Owner:
	name: str
	available_time: int
	preferences: List[str] = field(default_factory=list)
	pets: List[Pet] = field(default_factory=list)

	def add_pet(self, pet: Pet) -> None:
		pass

	def remove_pet(self, pet_name: str) -> None:
		pass

	def get_all_tasks(self) -> List[Task]:
		pass


class Scheduler:
	def generate_schedule(self, owner: Owner) -> None:
		pass

	def sort_tasks(self, tasks: List[Task]) -> List[Task]:
		pass

	def explain_plan(self) -> str:
		pass

