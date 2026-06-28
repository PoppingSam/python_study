# While循环
# 初始值
# 结束条件
# 变量要有变化
# while...else 和 for...else，else的特点：整个循环结束后执行的语句，如果被中断，则不执行

# break:跳出循环; continue:跳过本轮循环(跳过下面的语句),继续下一轮

# print 默认自动换行，如果不想换行可以加end = ""

''' 循环嵌套:
if 条件:
    pass
else:
    if 条件:
        pass

While 循环

'''



n = 1
while n <= 50:
    if n % 3 == 0: 
        print(n)
    n += 1

n = 0
while n <= 49:
    n += 1
    if n % 3 == 0:
        print(n)

n = 1
j = 0
while n <= 10:
    j += n
    n += 1
print(j)


n = 1
while n <= 10:
    n += 1

numbers = [1,2,3,4,5,6,7,8,9,10]
sum(numbers)

'''
输入用户名和密码,提示输入3次错误,账户被锁定
'''
for count in range(3):
    username = input("输入用户名")
    password = input("输入密码")

    if username == "admin" and password == "1234":
        print("登录成功")
        break
    print("用户名或密码有误")
else:
    print("账户被锁定")

# ===============
n = 1
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1
else:
    print("over")

# ===============
'''
不打印能被3整除
'''
for i in range(10):
    if i % 3 == 0:
        continue
    else:
        print(i)