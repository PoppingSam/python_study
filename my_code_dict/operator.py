# 1：输入1个3位整数，输出个位数，十位数，百位数
number = int(input("请输入1个3位整数: "))

print("个位数:", number % 10)
print("十位数:", number % 100 // 10) # 先用100取余，剩余两位数，再取整
print("十位数:", number // 10 % 10)  # 先用10取整，剩余两位数，再取余
print("百位数:", number // 100)

# =================================
# 2：求1-10的累加和
n = 1
j = 0
while n <= 10:
    j += n
    n += 1
print(j)

# =================================
# 4位验证码
import random

# 创建取值表
file = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"

#建立验证码初始值
code = ""

for i in range(4):
# 获取index随机值
    index = random.randint(0,len(file)-1)
    
# 通过index返回取值表内容
    code += file[index]
print(code)