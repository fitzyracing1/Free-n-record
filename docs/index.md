# Free(n) Computing Platform

Free(n) is a proposed protocol in which every unit of work is a task under one adaptive state model, `State = (n, i, context)`. Here `n` is depth or resource intensity, `i` is the iteration counter, and `context` carries state. It is meant as a base interaction format between classical and quantum computers in resource-constrained settings such as Mars.

The repository is mostly specification. The only runnable code is a Python reference runtime and a Mars demo.

## Getting started

```bash
python3 runtime/python/free_n.py    # demo: three dependent tasks, prints the final state
python3 mars/free_n_mars.py         # Mars demo, prints the final state and context keys
```

The `runtime/cpp`, `runtime/javascript` and `runtime/rust` folders contain only READMEs that list "planned contents".

## Documentation map

| Doc | Topic |
|---|---|
| `docs/SPEC.md`, `reference/specification.md` | specification |
| `docs/KERNEL.md`, `docs/RUNTIME.md`, `docs/SCHEDULER.md` | runtime design |
| `docs/LANGUAGE.md`, `examples/*.free` | `.free` task language |
| `docs/QUANTUM.md` | quantum–classical interaction format |
| `docs/FREE-N.md`, `docs/ROADMAP.md` | concept and roadmap |

Contributing: see `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`. There are no tests and no CI.

MIT License. Copyright (c) 2026 Joshua Almeida
