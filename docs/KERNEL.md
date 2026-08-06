# Free(n) Kernel

The Kernel is the minimal set of concepts that every Free(n) system must implement.

## Core Entities

### State
Immutable snapshot at any moment: `(n, i, context)`.  
Mutations produce a new State; the previous State may be retained for debugging or rollback.

### Task
A named unit of work with:
- a body (function / closure / computation)
- a list of dependency names
- optional resource hints (ignored by pure kernel, used by Resource Manager)

### Scheduler
Pure decision component. Given current State and Task registry, returns the next ready Task or signals that the graph is complete / blocked.

### Execution Engine
Invokes the Task body, captures the result, and returns control to the Runtime.

## Kernel Loop (conceptual)

```
state ← initial_state(n0, i=0, context={})
while true:
    task ← scheduler.next(state)
    if task is None:
        break
    if state.n < 0:
        break
    result ← engine.run(task, state)
    state.context[task.name] ← result
    state.i ← state.i + 1
    state.n ← adaptive_update(state.n, result, resources)   # optional
```

## Guarantees

- `i` never decreases.
- A Task runs only after all its dependencies have completed.
- The Kernel itself is deterministic given the same Task graph and the same adaptive policy.

## Non-Goals of the Kernel

- Network transport
- Persistence
- Concrete hardware mapping
- Security / sandboxing (left to higher layers)
