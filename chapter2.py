import cv2
import numpy as np
import matplotlib.pyplot as plt


im_path = 'test_ims/IMG_1904.jpg'
im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]
# gray = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
# h, w, _ = im.shape
# print(f'Height:{h}, Width:{w}')
# plt.imshow(im)
# plt.show()
# # 转成灰度图
# # 方式一：取一个通道
# gray = im[:, :, 0]
# # 方式二： 按比例加
# gray = 0.299*im[:, :, 0] + 0.587*im[:, :, 1] + 0.114*im[:, :, -1]
# print(f'Gray image shape:{gray.shape}')
# plt.imshow(gray, cmap='gray')
# plt.show()

# # test 2d gray im
# test_im = np.random.randint(0, 255, (3, 4),dtype=np.uint8)
# print(test_im)
# plt.imshow(test_im, cmap='gray')
# plt.show()

# # test 3d im
# test_im = np.random.randint(0, 255, (3, 4, 3),dtype=np.uint8)
# print(test_im)
# plt.imshow(test_im)
# plt.show()

# 8位整数图像 （会将所有数值转换进0-255之间）
# test_im = np.random.randint(0, 1000, (2, 2, 3))
# print(test_im)
# plt.imshow(test_im)
# plt.show()
# test_im_u8 = np.uint8(test_im)
# print(test_im_u8)
# plt.imshow(test_im_u8)
# plt.show()

# 图像相加--融合 or 加噪
# 图像相减--除去背景 比较差异 运用跟踪
# 图像相乘--mask
# 图像相除--校正设备 比较差异
imp1 = 'test_ims/IMG_1902.jpg'
imp2 = 'test_ims/IMG_1903.jpg'

im1 = cv2.imread(imp1, cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread(imp2, cv2.IMREAD_GRAYSCALE)
im_add = cv2.add(im1*0.5, im2*0.5)
im_plus = cv2.subtract(im1, im2)
im_div = cv2.divide(im1, im2)
plt.imshow(im_add, cmap='gray')
plt.show()

