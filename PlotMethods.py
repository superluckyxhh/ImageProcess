import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(2, 20)
y = 2 * x + np.random.randint(5, 20, 18)
plt.plot(x, y)
plt.show()

"""绘制线性图"""
x = np.linspace(0, 1, 100)
y1 = np.power(x, 3)
y2 = np.power(x, 1)
y3 = np.power(x, 0.5)
plt.plot(x, y1, label='3.0')
plt.plot(x, y2, label='1.0')
plt.plot(x, y3, label='0.5')
# 对三条线作标记
plt.legend()
# 添加横纵坐标的说明
plt.xlabel('confidence')
plt.ylabel('value')
# 增加表格形式
plt.grid()
# 限制两条坐标轴上的显示范围
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()


"""绘制柱状图"""
a = np.random.randint(0, 101, 1000)
bins = np.arange(-0.5, 100, 1)
plt.hist(a, bins, rwidth=0.8, color='green')
plt.show()