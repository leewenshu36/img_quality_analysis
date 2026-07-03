# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/7/31 23:02
# @Author: Lee Wen-tsao
# @E-mail: liwenchao36@163.com


import os, cv2


# 输出配置
ROOT = os.path.dirname(__file__)
output_dir = os.path.join(ROOT, "frame")



class ExtractFrame:
    def __call__(self, f_path, frame_step=1):
        # 路径校验
        if not os.path.isfile(f_path):
            raise FileNotFoundError(f"输入视频不存在: {f_path}!")

        # 参数校验
        if frame_step < 1:
            raise ValueError("frame_step 必须大于等于 1!")

        # 视频文件校验
        capture_obj = cv2.VideoCapture(f_path)
        if not capture_obj.isOpened():
            raise RuntimeError(f"无法打开视频文件：{os.path.basename(f_path)}!")

        # 视频帧数校验
        total_frame = int(capture_obj.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frame <= 0:
            capture_obj.release()
            raise RuntimeError(f"视频帧数无效: {f_path}!")

        fps = capture_obj.get(cv2.CAP_PROP_FPS)
        interval_frame = fps * 2
        half_interval = interval_frame // 2

        i = 0
        while True:
            ret, frame = capture_obj.read()

            if not ret: break

            if i % interval_frame == half_interval:
                img_path = os.path.join(output_dir, f"frame_{i}.png")
                cv2.imwrite(img_path, frame)
            i += 1

capture_frame = ExtractFrame()


if __name__ == "__main__":
    file_path = r"tar.mp4"
    capture_frame(file_path)



