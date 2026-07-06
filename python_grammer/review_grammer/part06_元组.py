'''
元组与列表类似, 不同之处在于元组的元素不能修改(增删改)
元组使用小括号(), 列表使用方括号[]
list 列表
tuple 元组 
'''

t1 = ()
print(type(t1)) # <class 'tuple'>

t2 = ("aa") # 元组括号内只有1个元素时，需要在元素后面加逗号, 否则会被认为时字符串
print(type(t2)) # <class 'str'>

t3 = ("aa",) # 元组括号内只有1个元素时，需要在元素后面加逗号, 否则会被认为时字符串
print(type(t3)) # <class 'tuple'>

t4 = ("aa", "bb", "cc", "aa") # <class 'tuple'>
print(type(t4))
len(t4)

# 索引和切片
print(t4[0])
print(t4[:2])
print(t4[::-1]) 

# 方法: index, count
t4.index("aa", 1, 3) # tuple.index("元素", 起始位置, 结束位置) 1表示从index: 1位置开始查找, 到3结束（不包含3的位置）
t4.count("aa")

# in, not in
if "cc" in t4:
    print("存在")

# 支持for...in 循环
for i in t4:
    print(i) 

# 转换
# list(tuple) 元组转列表
# tuple(list) 列表转元组
t4 = list(t4)
print(t4)

t4 = tuple(t4)
print(t4)