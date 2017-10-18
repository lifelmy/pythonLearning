
#数学函数
'''
a=22.22
import  math
print(math.modf(a))     #(0.21999999999999886, 22.0)，返回整数部分和小数部分
print(math.pow(10,3))   #10的三次方
print(round(123.126,2))  #四舍五入
print(math.ceil(9.1))    #向上取整
print(math.floor(9.1))   #向下取整
print(math.fabs(-10))   #取绝对值
print(abs(-1))          #取绝对值
print(math.sqrt(100))   #取平方根
'''

#随机函数
import random
print(random.random())  #随机生成下一个实数，它在[0,1)范围内
print(random.randrange(1,10,8)) #(开始位置，结束位置，步长)