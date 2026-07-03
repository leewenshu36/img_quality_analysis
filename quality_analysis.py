# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/7/31 23:02
# @Author: Lee Wen-tsao
# @E-mail: liwenchao36@163.com


import cv2
import numpy as np


class QualityAnalysis:
    @staticmethod
    def read_image(f_path):
        """读取图像"""
        image_byte = np.fromfile(f_path, np.uint8)
        image = cv2.imdecode(image_byte, cv2.IMREAD_COLOR)
        return image

    @staticmethod
    def crop_background(image):
        # 转灰度图像
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)

        # 边缘识别
        edges = cv2.Canny(image_blurred, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
            image = image[y: y+h, x:x+h]
        return image

    def __call__(self, f_path, *args, **kwargs):
        # 读取图像
        image = self.read_image(f_path)

        # 去背景
        image = self.crop_background(image)
        pass

if __name__ == "__main__":
    from image_quality_checker import analyze_blur

    image_path = r"E:\deep-learn\imgs\c50063c000e5466f9eb52e5c018df94f.jpg"

    result = analyze_blur(image_path)

    print(f"Blur Ratio: {result['blur_ratio']:.2f}%")
    print(f"Category: {result['category']}")
    print(f"Overall Blur: {result['overall_blur']}")