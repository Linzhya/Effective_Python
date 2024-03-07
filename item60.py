import asyncio
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


async def game_logic(state, neighbors):  # 定义状态变化逻辑
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


async def step_cell(y, x, get, set):  # 更新单个网格状态的方法
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = await game_logic(state, neighbors)
    set(y, x, next_state)


async def simulate(grid): #更新整张网格的状态
    next_grid = Grid(grid.height, grid.width)  # 注意，这里实例化了新的下一代类

    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(y, x, grid.get, next_grid.set) # Fan out
            tasks.append(task)

    await asyncio.gather(*tasks)  #Fan in
    return next_grid

# class ColumnPrinter:
#     def __init__(self):
#         self.grid = Grid(5, 9)
#         self.grid.set(0, 3, ALIVE)
#         self.grid.set(1, 4, ALIVE)
#         self.grid.set(2, 2, ALIVE)
#         self.grid.set(2, 3, ALIVE)
#         self.grid.set(2, 4, ALIVE)

#     def __str__(self):
#         return self.grid.__str__()



grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)


for i in range(5):
    print(grid)
    grid = asyncio.run(simulate(grid))