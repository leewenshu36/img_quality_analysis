# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/7/31 23:02
# @Author: Lee Wen-tsao
# @E-mail: liwenchao36@163.com

import os
from imagededup.methods import CNN


ROOT = os.path.dirname(__file__)
frame_dir = os.path.join(ROOT, "frame")


class DropDuplicate:
    def __call__(self, image_dir, *args, **kwargs):
        model = CNN()
        model.find_duplicates(image_dir=image_dir,
                              min_similarity_threshold=0.93,
                              scores=True,
                              outfile='results.json')

drop_duplicate = DropDuplicate()


if __name__ == "__main__":
    drop_duplicate(frame_dir)

