from maze import read_image, matrix_to_image
from maze_solver import bfs, a_star
from utils import re_path, find_point, save_solution
import copy
import time

def main():
    filename = str(input("nhap ten anh : "))
    maze = read_image(filename)

    maze1 = copy.deepcopy(maze)

    start, goal = find_point(maze)

    # loi giai 1
    maze_copy_1 = copy.deepcopy(maze)
    st1 = time.time()
    a_star_solution = a_star(maze_copy_1, start, goal)
    print(a_star_solution)
    et1 = time.time()
    save_solution(a_star_solution, "a_star", filename, et1-st1)


    # loi giai 2
    maze_copy_2 = copy.deepcopy(maze)
    st2 = time.time()
    bfs_solution = bfs(maze_copy_2, start, goal)
    et2 = time.time()
    save_solution(bfs_solution, "bfs", filename, et2-st2)



if __name__ == '__main__':
    main()

