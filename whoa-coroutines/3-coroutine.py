import time
from pprint import pprint
from typing import List, Iterable, Set, Generator, Any, Coroutine
from random import randint
from uuid import uuid4

def sleep(duration: int) -> Generator[str, None, None]:
    threshold = time.time() + duration
    #while (now := time.time()) <= threshold:
    while True:
        now = time.time()
        yield
        if now >= threshold :
            break

    return f"{duration=}"

def foo(task_id: str, x: int) -> Generator[tuple, None, None]:
    print(f"[{task_id=}] Starting...")
    prev = time.time()
    result = yield from sleep(x)
    print(f"[{task_id=}] Completed. Took {time.time() - prev:.3}sec")
    return f"{task_id=}", f"{result=}"

def wait(tasks: Iterable[Generator]) -> List[Coroutine]:
    pending = list(tasks)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                tasks[gen] = e.args[0]
                pending.remove(gen)

    print(f"duration = {time.time() - before:.3}")
    return list(tasks.values())

def main() -> int:
    tasks = [foo(str(i), randint(1, 3)) for i in range(10)]
    result = wait(tasks)
    pprint(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
