from queue import Queue
from queue import PriorityQueue
import cv2
import numpy as np

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

            if 0 <= new[0] < rows and 0 <= new[1] < cols and maze[new[0]][new[1]] != 0:
                new_g = g[current] + 1

                if new_g < g.get(new, float('inf')):
                    came_from[new] = current
                    g[new] = new_g
                    f[new] = new_g + heuristic(new, goal)
                    open_set.put((f[new], new))

    return None

def re_path(maze, came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    for i in path:
        maze[i[0]][i[1]] = 2

    return path

def read_image(filename):
    # Đọc ảnh thành ảnh xám
    image = cv2.imread(f'data/maze_image/{filename}.png', cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Không thể đọc ảnh: {filename}")
        return None  # Hoặc xử lý lỗi tùy ý

    # Chuyển ảnh thành ma trận nhị phân 0 và 1
    _, binary_matrix = cv2.threshold(image, 127, 1, cv2.THRESH_BINARY)

    # Lưu ma trận nhị phân vào tệp văn bản (nếu cần)
    # np.savetxt(f"data/maze_text/{filename}.txt", binary_matrix, fmt='%d')

    # Trả về ma trận nhị phân
    return binary_matrix
def find_point(maze) :
    start = None
    goal = None

    rows, cols = len(maze), len(maze[0])

    ls = 0
    rs = cols
    for i in range(cols):
        if maze[0][i] == 1:
            ls = i
            break
    for i in range(cols-1, -1, -1):
        if maze[0][i] == 1:
            rs = i
            break
    start = (0,(ls+rs)/2)

    lg = 0
    rg = cols
    for i in range(cols):
        if maze[0][i] == 1:
            ls = i
            break
    for i in range(cols - 1, -1, -1):
        if maze[0][i] == 1:
            rs = i
            break
    goal = (-1, (lg + rg) / 2)

    return start, goal
maze = read_image("maze1")

start, end = find_point(maze)
a_star(maze,start,end)