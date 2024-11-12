from queue import Queue
from utils import re_path
from queue import PriorityQueue
from maze import read_image,matrix_to_image
# bfs tim duong di ngan nhat
def bfs(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    came_from = {}
    visited = [[0] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = Queue()

    q.put((start, 0))
    visited[start[0]][start[1]] = 1

    while not q.empty():
        current, step = q.get()

        if (current == goal):
            return re_path(maze, came_from, current)

        for d in directions:
            new = (current[0] + d[0], current[1] + d[1])

            if 0 <= new[0] < cols and 0 <= new[1] < rows and visited[new[0]][new[1]] == 0:
                if maze[new[0]][new[1]] == 1:
                    came_from[new] = current
                    visited[new[0]][new[1]] = 1
                    q.put((new, step + 1))

    return None

# _star tim duong di ngan nhat
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(maze, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(maze)
    cols = len(maze[0])

    open_set = PriorityQueue()
    open_set.put((0, start))  # fn va vitri

    came_from = {}
    g = {start: 0}
    f = {start: heuristic(start, goal)}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return re_path(maze, came_from, current)

        for d in directions:
            new = (current[0] + d[0], current[1] + d[1])

            if 0 <= new[0] < rows and 0 <= new[1] < cols and maze[new] != 0:
                new_g = g[current] + 1

                if new_g < g.get(new, float('inf')):
                    came_from[new] = current
                    g[new] = new_g
                    f[new] = new_g + heuristic(new, goal)
                    open_set.put((f[new], new))

    return None



# maze = read_image("maze1")
#
# start = None
# goal = None
#
# for i in range(len(maze[0])):
#     if maze[0][i] == 1:
#         start = (0,i)
#         break
#
# for j in range(len(maze[0])-1,-1,-1):
#     if maze[len(maze)-1][j] == 1:
#         goal = (len(maze)-1,j)
#         break
#
# a = a_star(maze,start,goal)
#
# print(a)