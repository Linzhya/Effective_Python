"""采用queue的方式，不必像原来的方法，每推进一代，就新建一批线程，
而是可以提前创建数量固定的一组工作线程，当这组线程平行地处理完之后，等待一下批任务
"""
from collections.abc import Callable
from queue import Queue
from threading import Thread
from typing import Any, Iterable, Mapping
ALIVE = '*'
EMPTY = '_'


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        matrix_str = ""
        for row in self.rows:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str


def count_neighbors(y, x, get):  # 计算周围八个格子的alive数量
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y+0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y+0, x-1)
    nw = get(y-1, x-1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # Cause the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def fun(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


in_queue = ClosableQueue()
out_queue = ClosableQueue()


def count_neighbors(y, x, get):  # 计算周围八个格子的alive数量
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y+0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y+0, x-1)
    nw = get(y-1, x-1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def game_logic(state, neighbors):  # 定义状态变化逻辑
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)


class SimulationError(Exception):
    pass


# Start the threads upfront
threads = []
for _ in range(5):
    thread = StoppableWorker(game_logic_thread, in_queue, out_queue)
    thread.start()
    threads.append(thread)


def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))

    # in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    return next_grid


grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)


for i in range(5):
    print(grid)
    grid = simulate_pipeline(grid, in_queue, out_queue)

for thread in threads:
    in_queue.close()
for thread in threads:
    thread.join()
