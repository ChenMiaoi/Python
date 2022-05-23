import pandas as pd
import numpy as np

# 常用数据类型
# Series 一维，带标签(索引)数组
# DataFrame 二维，Series容器
a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(a)
print(type(a))

# 可以指定索引使用index,但是需要注意，索引的数量要和元素的个数匹配
b = pd.Series([1, 2, 3], index = list([3, 2, 1]))
print(b)

# 可以使用字典来快捷自定义索引
t_dict = {"name" : "lily", "age" : 18, "tel" : 10086}
c = pd.Series(t_dict)
print(c)

# 修改元素默认类型dtype
d = pd.Series([1, 2, 3], dtype = float)
print(d)
print(d.dtype)

# pandas依旧也有切片索引的操作
print(a[ : : 2])

# pandas的内置属性index, values
print(d.index)
print(d.values)

# 可以使用index配合for循环
for i in a.index :
    print(i)

# where方法, where(condition1, condition2)如果条件一满足，就不变，如果不满足，就设置为条件二
a = pd.Series(range(10))
print(a.where(a > 5, 10))

# DataFrame
a = pd.DataFrame(np.arange(12).reshape(3, 4))
print(a)
print(type(a))

# 行索引，横向索引，index， 0轴， axis = 0
# 列索引，纵向索引，colnumns， 1轴， axis = 1
b = pd.DataFrame(np.arange(12).reshape(3, 4), index = list([3, 2, 1]), columns = list([4, 3, 2, 1]))
print(b)