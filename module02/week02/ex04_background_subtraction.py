import numpy as np
import cv2


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2GRAY)


def compute_binary_mask(difference_single_channel):
    _, difference_binary = cv2.threshold(
        difference_single_channel, 15, 255, cv2.THRESH_BINARY)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    binary_mask = cv2.cvtColor(binary_mask, cv2.COLOR_GRAY2BGR)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


bg1_image = cv2.imread('./module02/week02/GreenBackground.png')
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('./module02/week02/Object.png')
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('./module02/week02/NewBackground.jpg')
bg2_image = cv2.resize(bg2_image, (678, 381))

difference_single_channel = compute_difference(bg1_image, ob_image)
cv2.imshow('Difference', difference_single_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

binary_mask = compute_binary_mask(difference_single_channel)
cv2.imshow('Binary mask', binary_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()