import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def conv(gray, kernel):
    H, W = gray.shape
    h, w = kernel.shape
    new_H = (H - h) + 1
    new_W = (W - w) + 1
    new_gray = np.zeros((new_H, new_W), dtype=np.uint8) 
    
    for i in range(new_H):
        for j in range(new_W):
            new_gray[i, j] = np.sum(gray[i:i+h, j:j+w] * kernel)
    return new_gray

def save_im(save_path, im):
    cv2.imwrite(save_path, im)

def generate_gaussian(kernel_size, sigma):
    sum_value = 0
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    for i in range(kernel_size):
        for j in range(kernel_size):
            x = i - center
            y = j - center
            kernel[i, j] = np.exp(-(x**2 + y**2)/(2 * sigma**2))
            sum_value += kernel[i, j]

    return kernel * (1 / sum_value)


def main():
    save_dir = 'plot_ims'
    im_path = 'test_ims/IMG_1895.jpg'
    im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]
    gray_im = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
   
    gaussian_kernel = generate_gaussian(3, 1.5)
    print(gaussian_kernel)

    gray_gaussian = conv(gray_im, gaussian_kernel)
    print(gray_gaussian)
main()
