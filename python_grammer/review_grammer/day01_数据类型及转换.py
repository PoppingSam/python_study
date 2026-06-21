#==========================
# 练习1
# 三引号是保留格式输出
shi = '''
            静夜思
           唐  李白
          床前明月光，
          疑是地上霜。
          举头望明月，
          低头思故乡。
'''
print(shi)

#==========================================
# 练习2
# 输入两个数，输出两数之和与差
number1 = input("第1个数: ")
number2 = input("第2个数: ")

print(float(number1) + float(number2))
print(float(number1) - float(number2))
print(int(float(number1)) - int(float((number2))))

# bool值转int，显示1或0，转字符串类型变为单词“True”
flag = True
print(int(flag))
print(str(flag))

# 当变量是0和""(空字符串)时，bool类型是False，其他只要变量有值bool类型是True
a = ""
b = -5
print(bool(a))
print(bool(b))