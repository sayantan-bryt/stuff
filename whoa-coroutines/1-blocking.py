import time
from pprint import pprint
from typing import List, Iterable, Set, Any
from random import randint
from uuid import uuid4

class Task:
    result: tuple = (None, None)
    def run(self):
        raise NotImplementedError()

class Sleep(Task):
    def __init__(self, duration: int):
        self.task_id: str = uuid4().hex
        self.duration: int = duration
        self.result: tuple = (None, None)
        self.started: float = 0

    def run(self) -> str:
        self.started = time.time()
        print(f"[Task: {self.task_id}] Starting")
        time.sleep(self.duration)
        print(f"[Task: {self.task_id}] Completed. Took {time.time() - self.started:.3}sec")
        self.result = (self.task_id, self.duration)
        return self.task_id

def wait(tasks: Iterable[Task]) -> List[Any]:
    orig: List[Task] = list(tasks)
    pending: Set[Task] = set(orig)
    before = time.time()

    while pending:
        for task in list(pending):
            task.run()
            pending.remove(task)

    print(f"Total duration = {time.time() - before:.3}")
    return [task.result for task in orig]



def main() -> int:
    tasks = [Sleep(randint(1, 3)) for _ in range(10)]
    result = wait(tasks)
    pprint(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
