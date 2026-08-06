# Free(n) Computing Platform – Canonical Reference

This document is the short-form canonical statement of the Free(n) protocol.

## State

```
State ≜ (n : ℤ, i : ℕ₀, context : Map)
```

## Execution Rule

```
if n ≥ 0 then
    result ← execute(current_task, State)
    context ← context ∪ {current_task.name ↦ result}
    i ← i + 1
    optionally adapt n
else
    terminate
```

## Invariants

1. `i` is strictly non-decreasing.
2. A task executes only after all its named dependencies have completed.
3. The interpretation of `n` is the responsibility of the Runtime, not the task author.
4. The protocol is language-neutral.

## Minimal Required Components

- State carrier
- Task registry with dependency lists
- Scheduler that returns only ready tasks
- Execution engine that applies the rule above

Any system that provides these components and obeys the four invariants is a conforming Free(n) implementation.

## Version

0.1 (initial public specification)
