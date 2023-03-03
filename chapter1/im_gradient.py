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


def main():
    save_dir = 'plot_ims'
    im_path = 'test_ims/IMG_1895.jpg'
    im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]
    gray_im = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
   
    X = np.linspace(-1, 1, 3)
    Y = np.linsapce(-1, 1, 3)
   

    # plt.subplot(131), plt.imshow(gray_im, cmap='gray'), plt.title('Origin')
    # plt.subplot(132), plt.imshow(gray_sobelx, cmap='gray'), plt.title('GradientX')
    # plt.subplot(133), plt.imshow(gray_sobely, cmap='gray'), plt.title('GradientY')
    # plt.show()



    

main()