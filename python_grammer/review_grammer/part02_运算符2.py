# 赋值运算符========================
# +=, -=, *=, /=, &=, //=, **=
a = 8
b = 4
c = 5
d = 3
e = 7
f = 26
a += 1
b *= 2
c //= 3
d **= 3
e %= 4
f /= 5
print(a, b, c, d, e, f)

b *= d
print(b)

# 关系运算符========================
# ==, >=, <=, !=

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)

d = "abc"
e = "abd"

# 字符串也可以比较，比较的是字符串对应的ASCII的码值，从字符串的第一个字符开始比较
print(d < e)

a = 1
b = 3
c = 0

# and 两边都是非0数字，取最后的数值
print(a and b)

# and 两边有1个数字为0，结果为0
print(a and c)

# and 原理：
# True and True ==> True
# True and False ==> False
# False and True ==> False
# False and False ==> False

# or 原理：其中一侧为True即为True
# True or True ==> True
# True or False ==> True
# False or True ==> True
# False or False ==> False

print(c or a)
print(b or a) # 适用于登录账号密码或手机验证码

n = 149
print(bin(n))

# 运算优先级：
# 算术运算符 + - * /
# 赋值运算符 += -=
# 比较运算符 >= <= !=
# 逻辑运算符 and or not
# 位运算符