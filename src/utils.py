import json
import numpy as np
import matplotlib.pyplot as plt

# dung lai duong di
def re_path(maze, came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()

    for i in path:
        maze[i[0]][i[1]] = 2

    return path

# tim diem start va goal cua ma tran vuong
def find_point(maze):
    start = None
    goal = None

    rows, cols = len(maze), len(maze[0])

    # Tìm điểm bắt đầu `start` ở dòng đầu tiên
    ls, rs = 0, cols - 1
    for i in range(cols):
        if maze[0][i] == 1:
            ls = i
            break
    for i in range(cols - 1, -1, -1):
        if maze[0][i] == 1:
            rs = i
            break
    start = (0, (ls + rs) // 2)

    # Tìm điểm kết thúc `goal` ở dòng cuối cùng
    lg, rg = 0, cols - 1
    for i in range(cols):
        if maze[rows - 1][i] == 1:
            lg = i
            break
    for i in range(cols - 1, -1, -1):
        if maze[rows - 1][i] == 1:
            rg = i
            break
    goal = (rows - 1, (lg + rg) // 2)

    return start, goal


# luu loi giai duoi dang file json
import json
import os

def save_solution(path, algorithm, output_name, _time):
    # Số bước là số lượng phần tử trong path
    steps = len(path)
    output_path = f"../results/{algorithm}/{output_name}.json"

    # Tạo thư mục nếu chưa tồn tại
    # os.makedirs(os.path.dirname(output_path), exist_ok=True)

    solution_data = {
        "algorithm": algorithm,
        "steps": steps,
        "solution": [f"({x}, {y})" for x, y in path],  # Lưu các bước giải
        "execution_time": _time  # Thời gian thực hiện thuật toán
    }

    # Lưu dữ liệu vào file JSON
    with open(output_path, 'w') as json_file:
        json.dump(solution_data, json_file, indent=4)

    print(f"Solution saved to {output_path}")


def create_plot(plot_name, x_axis, y_axis, y_value):
    x = np.arange(len(x_axis))
    width = 0.2

    fig, ax = plt.subplots()
    ax.bar(x-width/2, )

