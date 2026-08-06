"""
Free(n) Computing Platform – Minimal Python Reference Runtime
Version 0.1
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set


@dataclass
class State:
    n: int
    i: int = 0
    context: Dict[str, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"State(n={self.n}, i={self.i}, context_keys={list(self.context.keys())})"


class Task:
    def __init__(
        self,
        name: str,
        fn: Callable[[State], Any],
        deps: Optional[List[str]] = None,
        n_hint: Optional[int] = None,
    ):
        self.name = name
        self.fn = fn
        self.deps = deps or []
        self.n_hint = n_hint


class Scheduler:
    def __init__(self) -> None:
        self.tasks: Dict[str, Task] = {}
        self.completed: Set[str] = set()

    def register(self, task: Task) -> None:
        self.tasks[task.name] = task

    def mark_completed(self, name: str) -> None:
        self.completed.add(name)

    def ready(self) -> List[Task]:
        result = []
        for task in self.tasks.values():
            if task.name in self.completed:
                continue
            if all(d in self.completed for d in task.deps):
                result.append(task)
        return result

    def next(self, state: State) -> Optional[Task]:
        ready = self.ready()
        if not ready:
            return None
        # Simple policy: first ready task (registration order)
        return ready[0]


class Runtime:
    """
    Minimal Free(n) Runtime.

    Execution rule:
        if n >= 0:
            execute(task, n, i, context)
            i = i + 1
    """

    def __init__(self, initial_n: int = 0) -> None:
        self.state = State(n=initial_n)
        self.scheduler = Scheduler()

    def register(self, task: Task) -> None:
        self.scheduler.register(task)

    def execute(self, task: Task) -> Any:
        if self.state.n < 0:
            return None
        result = task.fn(self.state)
        self.state.context[task.name] = result
        self.scheduler.mark_completed(task.name)
        self.state.i += 1
        # Optional adaptive step (identity by default)
        # self.state.n = adaptive_policy(self.state)
        return result

    def run(self, max_steps: int = 100) -> State:
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
# Demo
# ---------------------------------------------------------------------------

def _demo() -> None:
    rt = Runtime(initial_n=2)

    def hello(state: State) -> str:
        msg = "Hello from Free(n)"
        print(f"[i={state.i}] {msg}")
        return msg

    def work(state: State) -> int:
        value = state.n * 10 + state.i
        print(f"[i={state.i}] work → {value}")
        return value

    def finish(state: State) -> str:
        print(f"[i={state.i}] finished with context={state.context}")
        return "done"

    rt.register(Task("hello", hello))
    rt.register(Task("work", work, deps=["hello"]))
    rt.register(Task("finish", finish, deps=["work"]))

    final = rt.run()
    print("Final state:", final)


if __name__ == "__main__":
    _demo()
