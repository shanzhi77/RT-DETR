# 基于轻量化RT-DETR-tiny的车辆小目标检测算法
PyTorch implementation of some single image small_car detect networks. 

Currently Implemented:


**Prerequisites:**
1. Python 3.8 
2. Pytorch 1.13.1+cu117
3. torchvision: 0.14.1+cu117
4. timm: 0.9.8
5. mmcv: 2.1.0
6. mmengine: 0.9.0



## Introduction
- **train.py** and **val.py** are the entry codes for training and testing, respectively.
- **get_FPS.py** contains image quality evaluation metrics, i.e., FPS.


## Quick Start
### datasets
```
通过网盘分享的文件：BDD100K-Urban nighttime.zip等2个文件
链接: https://pan.baidu.com/s/1aFMzUZwGReLdhlHW2i3zxQ?pwd=dvgm 提取码: dvgm 
--来自百度网盘超级会员v6的分享
```
### Train
```
python train.py
```
### Test
```
python test.py
```
