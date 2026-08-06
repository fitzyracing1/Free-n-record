# Free(n) Python Reference Runtime

Minimal, readable implementation of the Free(n) Computing Platform core loop.

## Requirements

- Python 3.9+

## Run the demo

```bash
python free_n.py
```

Expected output (approximate):

```
[i=0] Hello from Free(n)
[i=1] work → 20
[i=2] finished with context={...}
Final state: State(n=2, i=3, context_keys=[...])
```

## Using the Runtime

```python
from free_n import Runtime, Task, State

rt = Runtime(initial_n=1)

def my_task(state: State):
    print("Running at i =", state.i)
    return 42

rt.register(Task("my_task", my_task))
final_state = rt.run()
```

## What is demonstrated

- `State(n, i, context)`
- Task registration with dependencies
- Scheduler that respects deps
- Execution rule (`n >= 0` → execute → `i += 1`)
- Simple adaptive-ready loop

This is intentionally small so it can serve as a clear reference for other language implementations.
