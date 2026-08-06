# Free(n) Specification

**Version 0.1.1 – Draft**

## 1. Overview

Free(n) is a language-neutral adaptive computing protocol.  
A Free(n) system consists of a **State**, a **Scheduler**, a **Runtime**, a **Resource Manager**, an **Execution Engine**, and a **Task Graph**.

## 2. State Model

```
State = (n, i, context)
```

| Field     | Type          | Meaning |
|-----------|---------------|---------|
| `n`       | integer       | Control parameter (depth, priority, intensity, resource class). |
| `i`       | non-negative integer | Monotonic iteration / step counter. Incremented after every successful step, including the free/base case. |
| `context` | map / object  | Arbitrary key-value store holding intermediate results, configuration, and feedback. |

### Execution Rule (Unified)

```
if n <= 0:
    # free / base case  ("If n <=0 then n* free n =i++")
    result ← 1                  # multiplicative identity from original free_n
    i ← i + 1
else:
    result ← execute(task, n, i, context)
    i ← i + 1
    # optional adaptive adjustment of n
```

The base case still advances the global iteration counter. This keeps progress observable even when the control parameter has entered the free region.

## 3. Scheduler

The Scheduler maintains:

- A registry of named Tasks
- Dependency edges between Tasks
- The set of completed Task names

A Task may run only when all of its declared dependencies appear in the completed set.

The Scheduler is responsible for selecting the next ready Task given the current State.

## 4. Runtime

The Runtime owns the current State and the Scheduler.  
It exposes:

- `register(task)`
- `execute(task_name)` or `run(task_graph)`
- Resource queries and adaptive decisions

Concrete runtimes exist for CPU, GPU, Cloud, Edge, Distributed clusters, and AI models.  
See `RUNTIME.md`.

## 5. Resource Manager

The Resource Manager answers:

- What compute capacity is currently available?
- What is the power / latency / cost budget?
- How should the current value of `n` be mapped onto physical resources?

It never appears in the task author’s source; it is an internal runtime component.

## 6. Execution Engine

The Execution Engine is the component that actually invokes a Task’s body with the current State and returns a result that is written into `context`.

## 7. Task Graph

A Task Graph is a directed acyclic graph (DAG) of Tasks.  
Edges represent data or control dependencies.  
The graph may be static or dynamically extended by tasks themselves (subject to runtime policy).

## 8. Dependency Model

Dependencies are named.  
A Task declares the names of Tasks that must have completed before it may run.  
The Scheduler enforces this rule strictly.

## 9. Feedback Loop

After each successful step (including base case):

1. Result is stored in `context`
2. `i` is incremented
3. Optional adaptive function may adjust `n` based on observed cost, quality, or resource pressure
4. Scheduler is asked for the next ready Task

This forms the core adaptive feedback loop of Free(n).

## 10. Plugin System

Runtimes may load plugins that:

- Provide new resource backends
- Implement specialized Schedulers
- Supply domain-specific Task types (AI, quantum, etc.)
- Add observability or tracing

Plugins must respect the State model and the execution rule.

## 11. Conformance

A conforming Free(n) implementation:

- Maintains a State of the form `(n, i, context)`
- Obeys the unified execution rule and always increments `i` after a step
- Provides a Scheduler that respects declared dependencies
- Treats Tasks as the unit of work

Language-specific surface syntax is not part of the core specification.
