# file nay dung de chuyen maze thanh ma tran 01 va chuyen tu ma tran thanh anh

import cv2
import numpy as np
from PIL import Image

# doc anh

def read_image(filename):
    # Đọc ảnh thành ảnh xám
    image = cv2.imread(f'../data/maze_image/{filename}.png', cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Không thể đọc ảnh: {filename}")
        return None  # Hoặc xử lý lỗi tùy ý

    # Chuyển ảnh thành ma trận nhị phân 0 và 1
    _, binary_matrix = cv2.threshold(image, 127, 1, cv2.THRESH_BINARY)

    # Lưu ma trận nhị phân vào tệp văn bản (nếu cần)
    np.savetxt(f"../data/maze_text/{filename}.txt", binary_matrix, fmt='%d')

    # Trả về ma trận nhị phân
    return binary_matrix


# chuyen ma tran thanh anh
def save_result_image(maze,alogorithm,filename):
    maze_array = np.array(maze, dtype=np.uint8)

    height, width = maze_array.shape

    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            if maze_array[i, j] == 0:
                rgb_image[i, j] = [0, 0, 0]
            elif maze_array[i, j] == 1:
                rgb_image[i, j] = [255, 255, 255]
            elif maze_array[i, j] == 2:
                rgb_image[i, j] = [0, 255, 0]
            elif maze_array[i, j] == 3:
                rgb_image[i, j] = [255, 0, 0]

    img = Image.fromarray(rgb_image, mode='RGB')
    img.save('../results/{}/{}_ans.png'.format(alogorithm,filename))
    img.show()






