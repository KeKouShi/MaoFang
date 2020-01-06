"""
1~100之间偶数和

Version :0.1
Author :KeKouShi

sum = 0
for x in (0,100,2):
	#sum =sum +x
	if x %2 ==0:
		sum =sum +x
print(sum)
"""
"""
1-100随机猜数字

Version :0.1
Author :KeKouShi


import random
answer = random.randint(1,100)
counter =0
while True:
	counter =counter +1
	number = int(input('请输入'))
	if number <answer:
		print('请大一点')
	elif number >answer:
		print('请小一点')
	else:
		print('答对了')
		break
print('总共猜了%d次'% counter)
"""

"""
输出乘法口诀

Version :0.1
Author :KeKouShi

"""
for i in range(1,10):
	for j in range(1,i+1):
		print('%d*%d=%d' %(i,j,i*j),end='\t')
	print()
