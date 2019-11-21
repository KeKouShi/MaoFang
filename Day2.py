"""
使用变量保存数据并进行运算

Version:0.1
Author:KeKouShi
"""
a = 321
b = 123
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
"""
使用type()检查变量类型

Version:0.1
Author:KeKouShi
"""
c = 1+5j
d = 'hello,world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""
使用input()函数获取键盘输入
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version:0.1
Author:KeKouShi
"""
x = int(input('x='))
y = int(input('y='))
print('%d + %d = %d' % (a,b,a+b))
print('%d - %d = %d' % (a,b,a-b))
print('%d * %d = %d' % (a,b,a*b))
print('%d / %d = %d' % (a,b,a/b))
print('%d // %d = %d' % (a,b,a//b))
print('%d ** %d = %d' % (a,b,a**b))
print('%d %% %d = %d' % (a,b,a%b))

