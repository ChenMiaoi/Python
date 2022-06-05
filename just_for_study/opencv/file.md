# OpenCv  

---  

## 模块  

- core模块实现了最核心的数据结构以及基本运算，如绘图函数、数组操作相关函数等
- highgui模块实现了视频与图像的读取、显示、存储等接口
- imgproc模块实现了图像处理的基本方法，包括图像滤波、图像的几何变换、平滑、阀值分割等

- features2d模块用于提取图像特征以及特征匹配，nonfree模块实现了一些专利算法，如sift特征
- objdetect模块实现了一些莫标检测的功能，经典的基于Haar、LBP特征的人脸检测，基于HOG的行人的等
- stitching模块实现了图像凭借功能
- FLANN模块包含口语爱苏近似最近邻搜索FLANN和聚类Clustering算法
- ml模块机器学习模块(SVM,决策树，Boosting等等)
- photo模块包含图像修复和图像去嘈两部分
- video模块针对视频处理，如背景分割、前景检测、对象跟踪等
- calib3d模块即Calibration(校准)3D,这个模块主要是相机校准和三维重建的内容
- G-API模块包含超高效的图像处理pipeline引擎  


## 图像的基础操作  

### 图像的IO操作(course01)

- 图像的读取

```python
import cv2

cv2.imread()
#cv2.IMREAD_COLOR 以彩色模式加载图像，任何图像的透明度都将被忽略。这是默认参数
#cv2.IMREAD_GRAYSCALE 以灰度模式加载图像
#cv2.IMREAD_UNCHANGED 包括alpha通道的加载图像模式
#可以使用1、0、-1来分别表示上面的三个参数
```

- 显示图像
```python
cv2.imshow()
# winname : 窗口名称
# mat : 图像名
# 注意：在调用显示图像的API后，需要调用cv2.waitKey()预留时间，否则会出现图像窗口闪退的情况
```
> 同时，也可以使用matplotlib来显示

```python
import matplotlib.pyplot as plt
plt.imshow()
```

- 保存图像

```python
import cv2

cv2.imwrite()
# filename : 文件名
# img : 要保存的图像
```

### 绘制几何图形(course02)

- 绘制直线

```python
import cv2

cv2.line(img, start, end, color, thickness)
# img : 要绘制直线的图像
# start, end : 直线的起点和终点
# color : 线条的颜色
# Thickness : 线条宽度
```  

- 绘制圆形

```python
import cv2

cv2.circle(img, center, radius, color, thickness)
# img : 要绘制圆形的图像
# center radius : 圆心和半径
# color : 线条的颜色
# Thickness : 线条宽度，为-1时生成闭合图案并填充颜色
```

- 绘制矩形

```python
import cv2

cv2.rectangle(img, pt1, pt2, color, thickness)
# img : 要绘制图形的图像
# pt1 pt2 : 分别代表矩形左上角和右下角坐标
# color : 线条的颜色
# Thickness : 线条宽度
```

- 向图像中添加文字

```python
import cv2

cv2.putText(img, text, org, fontFace, fontScale, color, thickness)
# text : 要写入的文本数据
# org : 文本的位置
# fontFace : 字体的类型
# fontScale : 字体的大小
```