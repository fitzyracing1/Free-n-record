"""
Free(n) Mars Base Package
-------------------------
Minimal classical ↔ quantum interaction package for Mars-class environments.

Free(n) is used as the common interaction format:
    State = (n, i, context)

Classical tasks and (simulated) quantum tasks share the same State.
n is adapted according to a simple power/thermal budget.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set
import random
import math


# ---------------------------------------------------------------------------
# Core Free(n) types (Mars-tuned)
# ---------------------------------------------------------------------------

@dataclass
class State:
    n: int
    i: int = 0
    context: Dict[str, Any] = field(default_factory=dict)
    # Mars-specific resource view (kept small on purpose)
    power_budget: float = 1.0      # 0.0 – 1.0
    thermal_headroom: float = 1.0  # 0.0 – 1.0

    def __repr__(self) -> str:
        return (f"State(n={self.n}, i={self.i}, "
                f"power={self.power_budget:.2f}, thermal={self.thermal_headroom:.2f})")


class Task:
    def __init__(
        self,
        name: str,
        fn: Callable[[State], Any],
        deps: Optional[List[str]] = None,
        kind: str = "classical",   # "classical" | "quantum"
    ):
        self.name = name
        self.fn = fn
        self.deps = deps or []
        self.kind = kind


class Scheduler:
    def __init__(self) -> None:
        self.tasks: Dict[str, Task] = {}
        self.completed: Set[str] = set()

    def register(self, task: Task) -> None:
        self.tasks[task.name] = task

    def mark_completed(self, name: str) -> None:
        self.completed.add(name)

    def ready(self) -> List[Task]:
        return [
            t for t in self.tasks.values()
            if t.name not in self.completed
            and all(d in self.completed for d in t.deps)
        ]

    def next(self, state: State) -> Optional[Task]:
        ready = self.ready()
        return ready[0] if ready else None


class MarsRuntime:
    """
    Base Free(n) runtime tuned for Mars.

    Execution rule (classical or quantum task):
        if n >= 0:
            execute(task, n, i, context)
            i = i + 1
            adapt n and resource view
    """

    def __init__(self, initial_n: int = 1) -> None:
        self.state = State(n=initial_n)
        self.scheduler = Scheduler()

    def register(self, task: Task) -> None:
        self.scheduler.register(task)

    def _adapt(self, task: Task, result: Any) -> None:
        """Simple Mars-oriented adaptive policy."""
        # Consume a little power / thermal headroom
        cost = 0.05 + 0.02 * max(0, self.state.n)
        if task.kind == "quantum":
            cost *= 1.5  # quantum steps are more expensive

        self.state.power_budget = max(0.0, self.state.power_budget - cost)
        self.state.thermal_headroom = max(0.0, self.state.thermal_headroom - cost * 0.8)

        # Lower n when resources are tight
        if self.state.power_budget < 0.3 or self.state.thermal_headroom < 0.3:
            self.state.n = max(0, self.state.n - 1)
        elif self.state.power_budget > 0.7 and self.state.n < 5:
            self.state.n += 1  # can afford more intensity

    def execute(self, task: Task) -> Any:
        if self.state.n < 0:
            return None
        result = task.fn(self.state)
        self.state.context[task.name] = result
        self.scheduler.mark_completed(task.name)
        self.state.i += 1
        self._adapt(task, result)
        return result

    def run(self, max_steps: int = 50) -> State:
        steps = 0
        while steps < max_steps:
            if self.state.n < 0:
                break
            task = self.scheduler.next(self.state)
            if task is None:
                break
            self.execute(task)
            steps += 1
        return self.state


# ---------------------------------------------------------------------------
# Example hybrid tasks (classical ↔ quantum hand-off)
# ---------------------------------------------------------------------------

def classical_prepare(state: State) -> Dict[str, float]:
    """Classical side: prepare parameters for a quantum step."""
    params = {
        "theta": 0.1 * state.n + 0.05 * state.i,
        "shots": max(10, 50 * state.n),
    }
    print(f"[classical i={state.i} n={state.n}] prepare → {params}")
    return params


def quantum_step(state: State) -> Dict[str, Any]:
    """
    Simulated quantum task.
    In a real system this would submit a circuit and collect measurements.
    n controls circuit depth / shot count.
    """
    params = state.context.get("classical_prepare", {"theta": 0.0, "shots": 10})
    theta = params["theta"]
    shots = int(params["shots"])

    # Toy measurement: probability of |1> ≈ sin²(theta)
    p1 = math.sin(theta) ** 2
    counts = {"0": 0, "1": 0}
    for _ in range(shots):
        if random.random() < p1:
            counts["1"] += 1
        else:
            counts["0"] += 1

    result = {
        "counts": counts,
        "estimated_p1": counts["1"] / shots,
        "n_used": state.n,
    }
    print(f"[quantum   i={state.i} n={state.n}] measure → p1≈{result['estimated_p1']:.3f}")
    return result


def classical_postprocess(state: State) -> float:
    """Classical side: refine the quantum result."""
    q = state.context.get("quantum_step", {})
    p1 = q.get("estimated_p1", 0.0)
    # Simple classical refinement
    refined = p1 * (1.0 + 0.01 * state.n)
    print(f"[classical i={state.i} n={state.n}] post → refined={refined:.4f}")
    return refined


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main() -> None:
    print("=== Free(n) Mars Base Package – classical ↔ quantum demo ===\n")

    rt = MarsRuntime(initial_n=2)

    rt.register(Task("classical_prepare", classical_prepare, kind="classical"))
    rt.register(Task("quantum_step", quantum_step,
                     deps=["classical_prepare"], kind="quantum"))
    rt.register(Task("classical_postprocess", classical_postprocess,
                     deps=["quantum_step"], kind="classical"))

    final = rt.run()
    print("\nFinal state:", final)
    print("Context keys:", list(final.context.keys()))


if __name__ == "__main__":
    main()
