# Free(n) Computing Platform

**Adaptive. Iterative. Resource-aware.**

Free(n) is an open computing protocol and specification that treats every piece of work as a task executing under a simple, adaptive state model.

```
State = (n, i, context)

if n >= 0:
    execute(n, i, context)
    i = i + 1
```

Everything is a task.  
Everything is iterative.  
Everything adapts to the resources that are actually available.

## Why Free(n) Exists

Modern computing is fragmented across CPUs, GPUs, clouds, edge devices, AI accelerators, and emerging quantum hardware. Most systems force the programmer to manage this complexity explicitly.

Free(n) provides a single, language-neutral abstraction:

- **n** controls depth, priority, or resource intensity.
- **i** is the monotonic iteration counter.
- **context** carries all intermediate state and results.

The runtime is free to interpret `n` according to available hardware, power budget, latency requirements, or model size. The same task description can therefore run on a phone, a cluster, or a future quantum backend without rewriting the core logic.

## Core Ideas

| Concept              | Description |
|----------------------|-------------|
| Adaptive Execution   | The value of `n` is interpreted by the runtime against current resources. Higher `n` may mean deeper search, larger model, more parallel workers, or higher precision. |
| Iterative Scheduling | Every successful step increments `i`. Progress is always measurable and deterministic. |
| Resource-Aware       | The runtime (not the task author) decides how to map `n` onto CPUs, GPUs, memory, network, or specialized accelerators. |
| AI-Native            | Tasks can be pure computation, neural inference, agent steps, or hybrid. The same state model applies. |
| Distributed          | A Free(n) task graph can be partitioned across nodes; each node maintains its own `(n, i, context)` view. |
| Future Quantum       | `n` can later abstract over quantum circuit depth or shot count while preserving the same protocol surface. |

## Long-Term Vision

Free(n) aims to become a lightweight, open standard in the same spirit as POSIX, OCI, or WebAssembly — a common substrate that many languages, runtimes, and hardware targets can share.

Version 0.1 focuses on the specification and a minimal Python reference.  
Version 1.0 will stabilize the task graph, dependency model, and plugin interface.  
Later versions introduce native distributed runtime and quantum backend abstractions.

## Repository Layout

```
README.md                 This file
LICENSE                   MIT
CONTRIBUTING.md
CODE_OF_CONDUCT.md

docs/
  SPEC.md                 Formal specification
  KERNEL.md               Core kernel concepts
  RUNTIME.md              Runtime architecture
  SCHEDULER.md            Scheduler design
  LANGUAGE.md             .free task language
  FREE-N.md               Deep dive on the Free(n) model
  ROADMAP.md              Version plan

examples/
  hello.free
  scheduler.free
  distributed.free
  ai.free

runtime/
  python/                 Minimal reference implementation
  rust/                   Placeholder
  cpp/                    Placeholder
  javascript/             Placeholder

reference/
  specification.md        Canonical reference text
```

## Quick Start (Python Reference)

```bash
cd runtime/python
python -m free_n
```

See `runtime/python/README.md` for details.

## Status

This repository is the official open specification for the Free(n) Computing Platform.

Initial commit: **Initial Free(n) Computing Platform specification**

## License

MIT © 2026 Joshua Almeida (fitzyracing1)
