# Free(n) Runtime Architecture

A Runtime is a concrete realization of the Free(n) Kernel for a particular execution environment.

## Supported Targets (v0.1+)

| Target          | Notes |
|-----------------|-------|
| CPU             | Default. Single- or multi-threaded. |
| GPU             | `n` may control batch size, precision, or number of streams. |
| Cloud           | Elastic scaling; `n` maps to instance class or worker count. |
| Edge            | Power- and latency-constrained; runtime must respect tight budgets. |
| Distributed     | Multiple nodes each maintain local State; global coordination via context exchange. |
| AI Models       | Tasks may be inference steps, agent actions, or training iterations. |

## Responsibilities

1. Own the current State.
2. Host the Scheduler and Execution Engine.
3. Query or own a Resource Manager.
4. Map the abstract value of `n` onto concrete resources.
5. Provide observability (optional but recommended).

## Adaptive Mapping of `n`

The runtime is free to interpret `n`. Examples:

- `n = 0` → cheapest / fastest / lowest-precision path
- `n = 1..k` → progressive increase in quality or parallelism
- large `n` → maximum available resources or deeper search

Negative `n` is a signal to stop or reduce.

## Reference Implementation

See `runtime/python/` for a minimal, readable Python runtime that demonstrates:

- State dataclass
- Task registration
- Dependency-aware Scheduler
- Simple adaptive feedback
- Execution loop

Other language folders (`rust/`, `cpp/`, `javascript/`) are placeholders for future reference implementations.
