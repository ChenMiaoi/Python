# numpy的底层是C，因此运行速度比较快
from queue import PriorityQueue
from re import A
from cupshelpers import Printer
import numpy as np
import math

# TODO 创建一个数组
a = np.arange(10)
print(a)
print(type(a))

# ! 对ndarray对象进行向量处理
print(np.sqrt(a))

# ! 对列表中的元素开平方
b = [3, 4, 9]
result = []
for i in b :
    result.append(math.sqrt(i))
print(result)
    
# TODO 使用array创建数组
# ! dtype = typename, ndmin = n, 指定类型和纬度
a = np.array([1,2,3,4])
print(a)
print(type(a))

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))

# TODO 使用arange(start, end, step, dtype)
a = np.arange(1, 11)
print(a)
print(type(a))

# TODO 随机数创建numpy.random.random(size=(row, col...)) 且从[0.0, 1.0)
a = np.random.random(size = 5)
b = np.random.random(size = (2,3))
c = np.random.random(size = (2,3,4)) # 两个三行四列
print(a)
print(b)
print(c)

# TODO 随机整数numpy.random.randint(low, high, size, dtype)最小，最大，个数
a = np.random.randint(0,5,3)
print(a)
print(type(a))

b = np.random.randint(5, 11, size = (3, 4))
print(b)

c = np.random.randint(2, 6, size = (2, 3, 4))
print(c)
print(c.dtype)

# TODO 创建一个(期望为0, 方差为1)正态分布np.random.randn(d0, d1,...,dn) d代表维度
a = np.random.randn(4)
print(a)

b = np.random.randn(4, 2)
print(b)

# TODO 创建一个指定的正态分布np.random.normal(loc, scale, size), loc期望，scale方差
a = np.random.normal(3, 4, size = (2, 3))
print(a)

'''
    ndarray.ndim        秩， 轴的数量或者维度的数量
    ndarray.shape       矩阵，n行m列
    ndarray.size        矩阵元素的总个数
    ndarray.dtype       对象的元素类型
    ndarray.itemsize    每个元素的大小，以字节为单位
    ndarray.flags       对象的内存信息
    ndarray.real        元素的实部
    ndarray.imag        元素的虚部
    ndarray.data        包含矩阵的缓冲区，但是一般不用这个属性
'''

# TODO 使用np.zeros(shape, dtype, order) -- 但是全部元素为0
a = np.zeros((2,3), dtype = int)
print(a)

# TODO 使用np.ones(shape, dtype, order) -- 但是全部元素为1
a = np.ones((2,3), dtype = int)
print(a)
print(type(a))

# TODO 使用np.empty(shape, dtype, order) -- 不会初始化，直接开辟指定形状
a = np.empty((2,3), dtype = int)
print(a) 

# TODO 使用np.linspace(start, num, endpoint, retstep, dtype)
'''
    start       序列的起始值
    stop        序列的终止值
    num         生成元素个数
    endpoint    如果为True，就包含终止值，默认是True
    retstep     如果为True就会显示间距，默认是True
'''
a = np.linspace(1, 10, 10)
print(a)

# TODO 使用np.logspace(start, stop, num, endpoint, base, dtype)
# ! base就是对数log的底数
a = np.logspace(1, 10, 10, base = 2)
print(a)
