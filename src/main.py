from maze import read_image, save_result_image
from maze_solver import bfs, a_star
from utils import re_path, find_point, save_solution
import copy
import time
import matplotlib.pyplot as plt
import numpy as np

def main():
    filename = str(input("nhap ten anh : "))
    maze = read_image(filename)

    maze1 = copy.deepcopy(maze)

    start, goal = find_point(maze)

    # loi giai 1
    maze_copy_1 = copy.deepcopy(maze)
    st1 = time.time()
    a_star_solution = a_star(maze_copy_1, start, goal)
    et1 = time.time()
    save_solution(a_star_solution, "a_star", filename, et1-st1)
    save_result_image(maze_copy_1,"a_star",filename)


    # loi giai 2
    maze_copy_2 = copy.deepcopy(maze)
    st2 = time.time()
    bfs_solution = bfs(maze_copy_2, start, goal)
    et2 = time.time()
    save_solution(bfs_solution, "bfs", filename, et2-st2)
    save_result_image(maze_copy_2, "bfs", filename)

    # ve bieu do so sanh hai thuat toan
    names = ["a_star", "bfs"]
    times = [et1-st1, et2-st2]
    steps = [len(bfs_solution), len(a_star_solution)]

    x = np.arange(2)

    fig, ax1 = plt.subplots()

    width = 0.2

    bar1 = ax1.bar(x-width/2, times, width, label='time', color='blue')
    ax1.set_ylabel('Đơn vị (s)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    bar2 = ax2.bar(x + width / 2, steps, width, label='steps', color='orange')
    ax2.set_ylabel('Đơn vị (step)', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    for bar in bar1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', color='blue')

    for bar in bar2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', color='orange')

    ax1.set_xticks(x)
    ax1.set_xticklabels(names)

    ax1.legend(loc='upper center')
    ax2.legend(loc='lower center')
    plt.title("so sanh bfs va a*")
    plt.show()


if __name__ == '__main__':
    main()

