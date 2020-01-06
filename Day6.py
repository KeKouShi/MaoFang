"""
输入M,N计算C(M,N)
m = int (input('m = '))
n = int (input('n='))
fm = 1
for num in range(1,m+1):
    fm *= num
fn =1
for num in range(1,n+1):
    fn *=num
fmn = 1
for num in range(1,m - n + 1):
    fmn *= num
print(fm // fn //fmn)
"""
"""
判断一个数是不是回文数
"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp>0:
        total = total * 10 + temp %10
        temp //= 10
    return total ==num
print(is_palindrome(345))
