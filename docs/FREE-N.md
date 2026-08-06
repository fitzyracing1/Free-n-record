# Free(n) – Deep Dive

## Origin

The Free(n) idea began as a compact adaptive protocol:

```
free_n(n):
    if n <= 0:
        return 1
    return n * free_n(n - 1)
```

This simple recursive form already encodes the essential properties:

- a control parameter `n`
- a clear base case
- iterative / recursive progress
- a result that grows with the investment of `n`

The Free(n) Computing Platform generalizes that insight into a full execution model for arbitrary tasks.

## Unified Rule (v0.1.1)

The platform now makes the base case and the iteration counter explicit and consistent with the original spirit:

```
if n <= 0:
    # free / base case
    # "n * free_n" collapses to the multiplicative identity
    result = 1
    i = i + 1
else:
    execute(task, n, i, context)
    i = i + 1
    # optional adaptive adjustment of n
```

This is the meaning of the compact statement:

**If n <= 0 then n * free_n = i++**

When the control parameter hits the free/base region, the system still advances the global iteration counter `i` and returns the identity value that the original factorial used.

## From Factorial to Platform

| Original free_n          | Platform Free(n)                          |
|--------------------------|-------------------------------------------|
| `n` = depth of recursion | `n` = resource / intensity control        |
| base case `n <= 0` → 1   | base case `n <= 0` → result=1, i++        |
| multiply & recurse       | execute task, always i++, then adapt      |
| pure function            | stateful context + feedback loop          |

The same spirit remains: **invest `n`, observe progress via `i`, adapt**.

## Why the Name

“Free” refers to the freedom of the runtime to interpret `n` according to the actual resources present.  
The task author does not hard-code “use 8 GPU streams” or “run on 32 cores”.  
The author only states the logical work; the platform is free to map it.

## Relationship to Existing Standards

Free(n) does not replace POSIX, containers, or WebAssembly.  
It sits one layer above them as a *task and adaptation* protocol that those technologies can host.

## Design Invariants

1. State is always `(n, i, context)`.
2. Successful work (including the free/base case) always increments `i`.
3. Adaptation happens *after* a step, never inside the pure task body (unless the task itself is the adaptive policy).
4. The protocol stays language-neutral.

These invariants keep Free(n) small enough to be a real standard.
