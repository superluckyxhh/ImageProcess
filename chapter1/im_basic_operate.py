"""
图像的基本操作
"""
import cv2
import matplotlib.pyplot as plt

def cv2_imshow(wd_name, im):
    cv2.imshow(wd_name, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_base(im_path): 
    im_gray = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
    im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]

    print(f'Gray image shape {im_gray.shape}')
    print('Gray image:', im_gray)
    print(f'Image shape {im.shape}')
    print('Image:', im)

    # opencv读出来的都是uint8类型
    print(f'Gray image dtype{im_gray.dtype}')
    print(f'Gray image maxv:{im_gray.max()} minv:{im_gray.min()}' )
    print(im.dtype)
    # 查看im底层是什么格式 type函数适用于查数据类型
    print(f'Image type:{type(im)}')

    # plt读取灰度图时 效果不对 原因是plt自己不能正确读取灰度 增加camp
    plt.imshow(im_gray, cmap='gray')
    plt.show()
    # plt展示彩色图时 cv2读取的通道顺序是BGR 需要调整
    plt.imshow(im)
    plt.show()

    cv2_imshow('gray im', im_gray)
    cv2_imshow('color im', im)

    B, G, R = cv2.split(im)
    print(f'Blue channel:{B}')
    cv2_imshow('B', B)
    im_copy = im.copy()
    im_copy[:,:,0] = 0
    im_copy[:,:,1] = 0
    cv2_imshow('r', im_copy)

def im_padding_show(im):
    im_border = cv2.copyMakeBorder(im, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=0)
    plt.subplot(121), plt.imshow(im), plt.title('Origin')
    plt.subplot(122), plt.imshow(im_border), plt.title('Constant')
    plt.show()

def compute_im(im, gray):
    light_gray = gray + 100
    print(f'Add gray image:{light_gray}')
    light_gray2 = cv2.add(gray, 100)
    print(f'Add gray image 2:{light_gray2}')
    plt.subplot(131), plt.imshow(gray, cmap='gray'), plt.title('Origin')
    plt.subplot(132), plt.imshow(light_gray, cmap='gray'), plt.title('add')
    plt.subplot(133), plt.imshow(light_gray2, cmap='gray'), plt.title('add2')
    plt.show()



def main():
    im_path = 'test_ims/IMG_1895.jpg'
    im = cv2.imread(im_path, cv2.IMREAD_COLOR)[:, :, ::-1]
    im_gray = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
    print('Gray image:', im_gray)
    image_base(im_path)
    # 图像的边界填充
    im_padding_show(im)
    # 数值计算
    compute_im(im, im_gray)

main()

