# Free(n) Mars Base Package

Minimal base package that uses Free(n) as the interaction format between classical and quantum (or quantum-inspired) computing resources on a Mars-class platform.

## Purpose

Provide a small, self-contained starting point for:

- Classical control of quantum or hybrid tasks under the Free(n) state model
- Resource-aware adaptation suitable for planetary surface constraints (power, thermal, radiation, delay)
- Clear classical ↔ quantum hand-off points expressed only through `(n, i, context)`

This is intentionally a **base** package — the smallest useful unit that can be extended into a full Mars computing stack.

## Contents

```
mars/
  README.md           This file
  free_n_mars.py      Reference runtime + example hybrid tasks
```

## Quick Start

```bash
cd mars
python free_n_mars.py
```

## Design Notes for Mars

- `n` is interpreted against a simple power / thermal budget.
- Quantum-style tasks are currently simulated (measurement outcomes drawn from a distribution).  
  Real quantum backends can be plugged in later by replacing the body of a quantum task.
- Communication delay is not simulated in this base package; a later layer can wrap Free(n) with delay-tolerant networking.
- Radiation and soft-error considerations are left to higher-level fault-tolerance plugins.

## Extending

Register additional classical or quantum tasks with the same Runtime.  
The State object remains the only shared medium between domains.
