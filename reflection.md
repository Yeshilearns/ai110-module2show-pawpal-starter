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

Throughout this project, I used AI tools like Visual Studio Copilot mainly and ChatGPT to guide my thinking when I got stuck or needed help structuring parts of the system. I used it for things like breaking down how to implement classes, understanding how to connect different components, and refining logic for features like sorting, filtering, and scheduling. The most helpful prompts were the ones where I asked for step-by-step explanations or ways to improve a specific part of my code, rather than just asking for full solutions.


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

There were moments where I didn't accept AI suggestions as-is. For example, some suggestions combined too much logic into a single method, which made the code harder to follow and less modular. I chose to separate responsibilites across classes like Owner, Pet, and Scheduler to keep the design clean. I evaluated A suggestions by testing them in my code, checking if they matched my design, and making sure I understood how they worked before keeping them.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested several core behaviors of the system, including marking tasks as complete, adding tasks to pets, sorting tasks by time, handling recurrings tasks, and detecting scheduling conflicts. These tests were important because they verified both the basic functionality and the more advanced features I added later, like recurring tasks and conflict detection. I also made sure to include edge cases, such as tasks with the same time, to ensure the system handled them correctly.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
 
 I would rate my confidence in the scheduler around 4 out of 5. While all my automated tests passed and the system worked correctly in my manual testing, I did run into some challenges earlier when refining the logic and writing test cases. I had to go back and rethink parts of my implementation to make sure everything behaved as expected. If I had more time, I would test additional edge cases like overlapping durations (not just exact time matches), larger numbers of tasks, and more complex recurring patterns. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

One part of the project I am most satisfied with is how the overall system came together, especially the Scheduler and how it integrates sorting, filtering and conflict detection. I also feel good about how the code is structured, since each class has a clear responsibility and the system is easy to follow.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the conflict detection logic to handle overlapping time ranges instead of only exact matches. I would also enhance the UI to make it more interactive and user-friendly, and possibly add features like editing or deleting tasks directly from the interface.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned from this project is how to balance using AI with my own understanding. AI was helpful for guidance and suggestions, but I still needed to think critically abou the design and make decision myself. This helped me become more confident in structuring systems, debugging issues, and making sure different parts of the code work together properly.