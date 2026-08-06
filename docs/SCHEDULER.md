# Free(n) Scheduler

## Role

The Scheduler decides *which* Task to run next given the current State and the Task Graph.

It never executes the Task; that is the job of the Execution Engine.

## Required Interface

```
register(task: Task) → void
next(state: State) → Task | None
mark_completed(name: str) → void
```

## Dependency Rule

A Task is *ready* if and only if every name in its dependency list is present in the completed set.

The Scheduler must never return a non-ready Task.

## Selection Policy

The core specification does not mandate a particular selection policy among ready Tasks.  
Common policies (implementations may choose):

- FIFO / registration order
- Priority based on a field inside the Task or inside `context`
- Heuristic based on current `n` or resource pressure
- Random among ready set (for exploration)

Whatever policy is chosen must be documented by the Runtime.

## Interaction with Adaptive Feedback

After a Task completes, the Runtime may change `n`.  
The Scheduler is then asked again for the next Task under the *new* State.  
This allows the system to become more or less aggressive as resources or quality feedback arrive.

## Deadlock & Termination

If the Scheduler returns `None` while incomplete Tasks remain, the graph is either finished or deadlocked.  
Runtimes should detect and report permanent blockage.
