a = 3
b = 2
c = a // b # 整除
d = a % b  # 取余
e = 2 ** 3 # 指数计算
print(a, b, c, d, e)
print(a, b, c, sep="#") # sep可以用来加分隔符

#========================
# 练习：输入1个3位整数，输出个位数，十位数，百位数

number = int(input("请输入1个3位整数: "))

print("个位数:", number % 10)
print("十位数:", number % 100 // 10) # 先用100取余，剩余两位数，再取整
print("十位数:", number // 10 % 10)  # 先用10取整，剩余两位数，再取余
print("百位数:", number // 100)