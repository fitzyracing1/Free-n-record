# Free(n) as Quantum–Classical Interaction Format

Free(n) is designed as a **base interaction format** between classical and quantum computers.

## Why a Common Format Is Needed

Classical and quantum systems speak different languages:

- Classical: deterministic steps, memory, control flow, floating-point or integer state.
- Quantum: unitary evolution, measurement, probabilistic outcomes, limited coherence time.

A shared control and state protocol is required so that a classical controller can schedule, parameterize, and receive results from quantum subroutines (and vice versa) without rewriting the entire stack for every hardware target.

## Free(n) Mapping

| Free(n) element | Classical role                          | Quantum role                                      |
|-----------------|-----------------------------------------|---------------------------------------------------|
| `n`             | Resource intensity / precision / depth  | Circuit depth, number of shots, ansatz complexity |
| `i`             | Iteration / step counter                | Shot index or variational iteration               |
| `context`       | Shared classical memory & results       | Measurement outcomes, parameters, feedback        |

### Execution Rule Reminder

```
if n >= 0:
    execute(task, n, i, context)   # task may be classical or quantum
    i = i + 1
```

A task body can be:

- pure classical computation,
- a quantum circuit submission + measurement,
- a hybrid variational step,
- a classical post-processing of quantum results.

The same State object carries the conversation between the two domains.

## Adaptive Behaviour

The runtime (or a higher-level agent) may raise or lower `n` after inspecting results in `context`:

- Low `n` → shallow circuits, few shots, low classical precision (power-saving / low-latency).
- High `n` → deeper circuits, more shots, higher classical refinement (when resources and coherence allow).

This makes Free(n) natural for resource-constrained environments such as planetary surface systems.

## Mars Relevance

On Mars the constraints are extreme: power, thermal, radiation, communication delay, and limited classical compute.  
Free(n) lets a classical Mars computer treat quantum co-processors (or future quantum sensors) as just another task type under the same adaptive state, without special-case orchestration code.
