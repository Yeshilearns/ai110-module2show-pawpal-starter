# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design was pretty straightforward and focused on keeping things modular and easy to understand. I used four main classes: Owner, Pet, Task, and Scheduler. The Owner class was meant to act as the top-level object that holds all the pets and keeps track of things like available time. Each Pet has its own list of tasks, so the Pet class mainly manages adding, removing, and accessing those tasks. The Task class represents individual activities like feeding or walking, with attributes like duration, priority, and completion status. The Scheduler was designed as the main logic component that takes all the tasks, organizes them, and generates a daily plan. So, I tried to keep each class focused on one responsibility so the system would be easier to extend later.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed during implementation as I added more functionality. Initially, the Task class only included basic attributes like title, duration, and priority, but as I worked on features like sorting, filtering, and recurring tasks, I realized additional fields were necessary. I added a time attribute to support sorting tasks chronologically, and a pet_name attribute so that tasks could still be associated with a specific pet even after being combined across all pets. Later, I introduced frequency and due_date to support recurring tasks, allowing the system to automatically generate future tasks. These changes made the system more realistic and flexible while still keeping the overall structure of the design intact.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

In my scheduler, the main constraints I considered were the owner’s available time, task priority, and whether a task was already completed. The scheduler first filters out completed tasks, then sorts the remaining ones based on priority, and finally selects tasks until the available time runs out. I focused mostly on priority and time because those felt the most realistic — in real life, a pet owner would want to make sure the most important tasks (like feeding or medication) are done first while staying within their limited time. Other features like sorting by time or filtering by pet help improve organization, but the core decision-making is really driven by priority and how much time is available.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is in conflict detection. It only checks if two tasks have exactly the same time, rather than checking for overlapping durations. This makes the implementation simple and efficient, but it may miss more complex conflicts where tasks overlap partially. I chose this approach to keep the logic easy to understand and maintain.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
