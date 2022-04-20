
# ! Exception例外，在编程中称之为异常
'''
    try...except是最常见的异常处理结构
    try:
        被监控的可能引发错误的代码
    except BaseException[as e]:
        异常处理
    
    如果try中异常了，从异常开始的以后的代码就会被跳过直接执行异常处理
'''

from tokenize import Name


try :
    print("step1")
    a = 3 / 0
    print("step2")
except :
    print("step3")
print("step4")

'''
# TODO 循环输入数字，不是数字就处理异常
while True :
    try :
        x = int(input("请输入一个数字:> "))
        print("输入的数字: ", x)
        if x == 88 :
            print("退出程序")
            break
    except :
        print("必须输入一个数字VALUE ERROR！")
'''

# TODO 多个except结构 ： 按照先子类后基类 -- 最好在最后面使用BaseException
try :
    a = input()
    b = input()
    c = float(a) / float(b)
except ZeroDivisionError :
    print("不能除以0")
except ValueError :
    print("不能将字符串转化为为数字")
except NameError :
    print("变量不存在")
except BaseException as e:
    print(e)
else :
    print(c)
finally :
    print("我是finally，无论如何都会实现")
    
# ! else结构，如果没有异常就执行else，有异常就执行except

# ! finally结构，finally结构内的代码无论如何都会被执行，通常用来释放try中申请的资源

