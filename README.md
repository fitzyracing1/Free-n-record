# Free(n) Computing Platform

**Base interaction format between quantum and classical computers.**  
**Adaptive. Iterative. Resource-aware. Ready for Mars.**

Free(n) is an open computing protocol that treats every piece of work as a task under a single adaptive state model:

```
State = (n, i, context)

if n >= 0:
    execute(task, n, i, context)   # classical or quantum
    i = i + 1
```

Everything is a task.  
Everything is iterative.  
Everything adapts to the resources that are actually available.

## Core Purpose

Free(n) is intended as a **base interaction format** between classical and quantum computers.  
The same State object carries parameters, measurement results, and control decisions across the classical–quantum boundary.  
`n` maps naturally onto classical intensity *and* quantum circuit depth / shot count.

This makes Free(n) especially suitable for constrained environments such as planetary surface systems (Mars), where power, thermal, radiation, and communication limits force continuous adaptation.

## Why Free(n) Exists

Modern computing is fragmented across CPUs, GPUs, clouds, edge devices, AI accelerators, and emerging quantum hardware. Most systems force the programmer to manage this complexity explicitly.

Free(n) provides a single, language-neutral abstraction:

- **n** controls depth, priority, or resource intensity (classical *and* quantum).
- **i** is the monotonic iteration / shot / step counter.
- **context** carries all intermediate state and results between domains.

The runtime is free to interpret `n` according to available hardware, power budget, thermal headroom, latency, or coherence time. The same task description can therefore run on a phone, a Mars lander, a cluster, or a quantum co-processor without rewriting the core logic.

## Core Ideas

| Concept              | Description |
|----------------------|-------------|
| Adaptive Execution   | `n` is interpreted by the runtime against current resources. Higher `n` may mean deeper circuits, more shots, larger classical models, or higher precision. |
| Iterative Scheduling | Every successful step increments `i`. Progress is always measurable. |
| Resource-Aware       | The runtime (not the task author) maps `n` onto CPUs, GPUs, quantum backends, power, and thermal limits. |
| Quantum–Classical    | Free(n) is the common conversation format between the two domains. |
| Mars / Space Ready   | Designed from the start for extreme resource constraints. |
| AI-Native            | Tasks can be pure computation, neural steps, agent actions, or hybrid. |
| Distributed          | Task graphs can be partitioned; each node keeps its own `(n, i, context)` view. |

## Repository Layout

```
README.md
LICENSE
CONTRIBUTING.md
CODE_OF_CONDUCT.md

docs/
  SPEC.md
  KERNEL.md
  RUNTIME.md
  SCHEDULER.md
  LANGUAGE.md
  FREE-N.md
  QUANTUM.md          ← quantum–classical interaction format
  ROADMAP.md

examples/
  hello.free
  scheduler.free
  distributed.free
  ai.free

runtime/
  python/             Minimal reference
  rust/  cpp/  javascript/   Placeholders

mars/                 ← Base package for Mars
  README.md
  free_n_mars.py      Classical ↔ quantum demo under Free(n)

reference/
  specification.md
```

## Quick Start

**Core Python reference**
```bash
cd runtime/python
python free_n.py
```

**Mars base package (classical ↔ quantum)**
```bash
cd mars
python free_n_mars.py
```

## Status

This repository is the official open specification for the Free(n) Computing Platform.  
Version 0.1 establishes the protocol and the first Mars-oriented base package.

## License

MIT © 2026 Joshua Almeida (fitzyracing1)

## Documentation

- In-repo docs: [docs/](docs/index.md)
- Wiki: [https://github.com/fitzyracing1/Free-n-record/wiki](https://github.com/fitzyracing1/Free-n-record/wiki)
