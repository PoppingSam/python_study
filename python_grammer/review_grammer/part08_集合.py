'''
Set集合:
特点: 没有重复, 无序的, 没有索引值
符号: {}, 当元素不是键值对时, 属于set
'''

set1 = {"a"} # 当花括号里不是键值对时, 属于set
print(type(set1))

# 去除重复值
list1 = [1, 3, 4, 3, 5, 7, 7, 8]
set2 = set(list1)
print(set2)
print(list(set2))

# 添加元素
set3 = set() # 声明空集合
set3.add("三体")
set3.add("盗墓笔记")
print(set3)

# 合并集合
set3.update(set1)
print(set3)

'''
产生5组不重复的4位验证码, 字母和数字组成
'''
import random

file = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
set4 = set()

while True:
    code = ""
    for i in range(4):
        number = random.choice(file)
        code += number
# 将code加入set中
    set4.add(code)
# 判断长度
    if len(set4) == 5:
        break
print(set4)

# 删除元素
set5 = {"三体", "红楼梦", "盗墓笔记", "西游记"}
set5.remove(6) # 如果元素不存在时, 会报错
print(set5)
set5.discard(6) # 如果元素不存在时, 不会报错
print(set5)
set5.clear() # 清空元素
print(set5)
set5.pop() # 随机删除元素
print(set5)

# 交集: intersection 并集: union 差集: difference
set6 = {1,2,3,4,5}
set7 = {3,4,5,6,7}

result = set6.intersection(set7)
print(result)

result = set6.union(set7)
print(result)

result = set6.difference(set7)
print(result)

result = set7.difference(set6)
print(result)

print(set6 | set7) # 并集的符号
print(set6 & set7) # 交集的符号
print(set6 - set7) # 差集的符号

'''
类型转换
list可以转tuple, set(长度可能发生改变)
tuple可以转list, set
set可以转list, tuple
dict可以转list, tuple, set 但只将键放进元素

特殊要求:
list1 = [("a", 1),("b",2),("c",3)] 或者 list1 = [["a", 1],[]"b",2],["c",3]]
可以转dict
'''