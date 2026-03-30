import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="User", available_time=120)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")

owner = st.session_state.owner
scheduler = st.session_state.scheduler

owner_name = st.text_input("Owner name", value=owner.name)
owner.name = owner_name

owner.available_time = st.number_input(
    "Available time today (minutes)",
    min_value=10,
    max_value=600,
    value=owner.available_time,
)

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Pet age", min_value=0, max_value=50, value=2)

if st.button("Add pet"):
    new_pet = Pet(name=pet_name, species=species, age=int(pet_age))
    owner.add_pet(new_pet)
    st.success(f"{pet_name} was added.")

if owner.pets:
    st.markdown("### Current Pets")
    pet_rows = [
        {"Name": pet.name, "Species": pet.species, "Age": pet.age}
        for pet in owner.pets
    ]
    st.table(pet_rows)
else:
    st.info("No pets added yet.")

st.divider()

st.markdown("### Tasks")
st.caption("Add tasks and connect them to a pet so they can be used by the scheduler.")

if owner.pets:
    selected_pet_name = st.selectbox(
        "Choose a pet for this task",
        [pet.name for pet in owner.pets]
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.number_input("Priority (1-5)", min_value=1, max_value=5, value=3)

    col4, col5, col6 = st.columns(3)
    with col4:
        task_time = st.text_input("Task time (HH:MM)", value="09:00")
    with col5:
        category = st.text_input("Category", value="Exercise")
    with col6:
        frequency = st.selectbox("Frequency", ["none", "daily", "weekly"], index=0)

    if st.button("Add task"):
        selected_pet = next((pet for pet in owner.pets if pet.name == selected_pet_name), None)

        if selected_pet:
            new_task = Task(
                title=task_title,
                duration=int(duration),
                priority=int(priority),
                category=category,
                time=task_time,
                frequency=None if frequency == "none" else frequency,
                due_date=date.today(),
            )
            selected_pet.add_task(new_task)
            st.success(f"Task '{task_title}' added for {selected_pet_name}.")
else:
    st.info("Add a pet first before adding tasks.")

all_tasks = owner.get_all_tasks()

if all_tasks:
    st.write("Current tasks:")
    task_rows = [
        {
            "Title": task.title,
            "Pet": task.pet_name,
            "Time": task.time,
            "Duration": task.duration,
            "Priority": task.priority,
            "Category": task.category,
            "Completed": task.completed,
            "Frequency": task.frequency or "one-time",
        }
        for task in all_tasks
    ]
    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a schedule using your scheduler logic and show warnings if conflicts exist.")

if st.button("Generate schedule"):
    all_tasks = owner.get_all_tasks()

    if not all_tasks:
        st.warning("No tasks available to schedule.")
    else:
        conflicts = scheduler.detect_conflicts(all_tasks)
        if conflicts:
            for warning in conflicts:
                st.warning(warning)

        schedule = scheduler.generate_schedule(owner)
        sorted_schedule = scheduler.sort_by_time(schedule)

        if sorted_schedule:
            st.success("Schedule generated successfully.")

            schedule_rows = [
                {
                    "Title": task.title,
                    "Pet": task.pet_name,
                    "Time": task.time,
                    "Duration": task.duration,
                    "Priority": task.priority,
                }
                for task in sorted_schedule
            ]

            st.markdown("### Today's Schedule")
            st.table(schedule_rows)

            st.markdown("### Scheduler Explanation")
            st.write(scheduler.explain_plan())
        else:
            st.warning("No tasks could fit within the available time.")