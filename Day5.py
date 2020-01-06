"""
找出水仙花数
Version:0.1

for num in range(100,1000):
	a = num %10
	b = num //10 % 10
	c = num //100
	if num == a**3 + b**3 +c**3:
		print(num)
"""
"""
正整数的反转

num = int(input('num = '))
a = 0
while num >0:
	a = a*10 +num %10
	num =num //10
print(a)
"""
"""
百钱百鸡


for x in range (0,20):
	for y in range (0,33):
		z=100-x-y
		if 5*x +3*y +z/3 ==100:
			print('公鸡:%d只，母鸡:%d只，小鸡:%d只'%(x,y,z))
"""
"""
CRAPS赌博游戏

"""
"""
CRAPS赌博游戏
"""
from random import randint
money = 1000
while money > 0:
        print('你的资产为',money)
        a = False
        while True:
            debt=int(input('清下注:'))
            if 0>debt<money:
                print('您的赌注不够，请重新下注')
            break
        first = randint(1,6)+randint(1,6)
        print('玩家摇出了%d点'%first)
        if first ==7 or first ==11:
                print('玩家胜')
                money = money +debt
        elif first ==2 or first ==3 or first ==12:
                print('庄家胜')
                money = money -debt
        else:
                a = True
        while a:
                a =False
                current =randint(1,6) + randint(1,6)
                print('玩家摇出了%d点'%current)
                if current ==7:
                        print('庄家胜')
                        money = money -debt
                elif current ==first:
                        print('玩家胜')
                        money = money +debt
                else:
                        a =True
print('你破产了，游戏结束')
