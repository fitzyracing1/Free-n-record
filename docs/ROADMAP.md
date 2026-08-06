# Free(n) Roadmap

## Version 0.1 (Current)

- Core specification (State, Scheduler, Runtime, Task Graph)
- Language-neutral documentation
- Minimal Python reference runtime
- Four illustrative `.free` examples
- **Quantum–classical interaction format** documented (`docs/QUANTUM.md`)
- **Mars base package** (`mars/`) – classical ↔ quantum hand-off under Free(n)
- Repository structure and community files

## Version 0.2

- Formal grammar for `.free`
- First-class dependency and data-passing model
- Basic observability / tracing hooks
- Additional language runtimes (Rust or JavaScript)
- Real quantum backend adapters (replace simulation in Mars package)

## Version 1.0

- Stable Task Graph and Plugin interfaces
- Conformance test suite
- Documented adaptive policies (including Mars power/thermal profiles)
- Reference distributed runtime (multi-node)
- Delay-tolerant networking layer for planetary distances

## Future

- AI orchestration primitives (agent steps, tool use, model selection under `n`)
- Quantum backend abstraction (`n` → circuit depth / shots / ansatz complexity)
- Radiation-aware and soft-error tolerant plugins
- Formal verification of the core loop
- Industry / standards-body engagement

The guiding principle remains: keep the core protocol small, adaptive, and free — suitable as the base interaction format between classical and quantum computers, including on Mars.
