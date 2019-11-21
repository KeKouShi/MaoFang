"""
分支，若输入的账号不为admin,密码不为123456，则提示输入错误

Version: 0.1
Author: KeKouShi
a = input('请输入用户名：')
b = input('请输入密码：')
if a == 'admin' and b == '123456':
	print('登录成功')
else:
	print('登录失败')	
"""
"""
分段函数求值

Version: 0.1
Author: KeKouShi

     3x -5 (x>1)
f(x)=x+2 (-1<=x<=1)
     5x+3 (x<=-1)
"""
x = float(input('x='))
if x >1:
	y=3*x-5
elif -1<=x and x<=1:
	y=x+2
else:
	y=5*x+3
print('f(x)=',y)
