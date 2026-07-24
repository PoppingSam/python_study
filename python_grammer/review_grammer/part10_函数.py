'''
函数作用: 复用
格式: 
def 函数名([参数1, 参数2]):  # 参数可以省略
    代码

函数名: 注意命名规范
代码： 封装重复内容
调用函数: 函数名（）
'''
# 生成验证码函数
import random

def generate_code():
    # 生成验证码
    code = ""
    s = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
    for i in range(4):
        char = random.choice(s)
        code += char
    print(code)

# 调用函数
generate_code()

# 定义1个login函数
# admin 1234

def log_in():
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == "admin" and password == "1234":
        print("登录成功")
    else:
        print("用户名或密码错误")

log_in()

'''
带参数的函数
def 函数名(参数1, 参数2, ....):
    pass
    
参数在调用函数时向函数传值
'''
import random

def generate_code(number):
    # 生成验证码
    code = ""
    s = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
    for i in range(number):
        char = random.choice(s)
        code += char
    print(code)

generate_code(6)

# ==============
def log_in(n):
    for i in range(n):
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        if username == "admin" and password == "1234":
            print("登录成功")
            break
        else:
            print("用户名或密码错误")
    else:
        print("账号被锁定")

log_in(2)