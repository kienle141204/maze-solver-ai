import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu
categories = ['Danh mục 1', 'Danh mục 2', 'Danh mục 3']
values_a = [10, 15, 7]  # Đối tượng A (đơn vị 1)
values_b = [80, 120, 50]  # Đối tượng B (đơn vị 2)

x = np.arange(len(categories))  # Vị trí của các cột
width = 0.3  # Độ rộng của mỗi cột

# Tạo Figure và trục chính (ax1)
fig, ax1 = plt.subplots()

# Vẽ biểu đồ cột cho Đối tượng A trên trục y chính (ax1)
bars1 = ax1.bar(x - width/2, values_a, width, label='Đối tượng A', color='blue')
ax1.set_ylabel('Đơn vị 1', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Tạo trục y thứ hai (ax2) và vẽ biểu đồ cột cho Đối tượng B
ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, values_b, width, label='Đối tượng B', color='orange')
ax2.set_ylabel('Đơn vị 2', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Thêm nhãn, tiêu đề và các chú thích
ax1.set_xlabel('Danh mục')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)
plt.title('Biểu đồ cột nhóm với hai trục y')

# Hiển thị giá trị trên đỉnh các cột của Đối tượng A
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='top', color='blue')

# Hiển thị giá trị trên đỉnh các cột của Đối tượng B
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom', color='orange')

# Thêm bảng chú thích cho cả hai trục
ax1.legend(loc='upper left')  # Chú thích cho trục y chính (ax1)
ax2.legend(loc='upper right')  # Chú thích cho trục y phụ (ax2)

plt.show()
