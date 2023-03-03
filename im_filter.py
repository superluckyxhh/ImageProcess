import cv2
import numpy as np
import matplotlib.pyplot as plt

def mean_filter(gray, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.int8)
    H, W = gray.shape
    for i in range(1, H-1):
        for j in range(1, W-1):
            v = np.sum(kernel * gray[i-1:i-1+kernel_size, j-1:j-1+kernel_size])
            v = v // 9
            gray[i, j] = v
    return gray



 
def main():
    im_path = 'test_ims/IMG_1895.jpg'
    im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]
    gray_im = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
    # mean_filter_gray = mean_filter(gray_im)
    mean_filter_gray2 = cv2.blur(gray_im, (3, 3))
    # plt.subplot(131), plt.imshow(gray_im, cmap='gray'), plt.title('origin')
    # plt.subplot(132), plt.imshow(mean_filter_gray, cmap='gray'), plt.title('meanfilter')
    # plt.subplot(133), plt.imshow(mean_filter_gray2, cmap='gray'), plt.title('cv2meanfilter')
    # plt.show()

    # 滤波的方法从操作都一样，不同的是每种方法的巻积核的构造不同
    gaussian_fliter_gray = cv2.GaussianBlur(gray_im, (3, 3), 1)
    # plt.subplot(121), plt.imshow(gray_im, cmap='gray'), plt.title('origin')
    # plt.subplot(122), plt.imshow(gaussian_fliter_gray, cmap='gray'), plt.title('gaussianfilter')
    # plt.show()

main()


    