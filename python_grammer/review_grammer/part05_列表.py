# 列表存储多个数据
list2 = ["牛奶", "面包", "鸡蛋", "水果", "蔬菜", "饮料", "零食"]

# 切片
print(list2[1:3])
print(list2[::-3])
print(list2[1:-1])
print(list2[2:-2])
print(list2[-2:-5:-2])
print(list2[::3])
print(list2[:4:3] + [list2[-3]])

s = 'abcd123'
d = 0
while True:
    for i in s:
        if i.isdigit():
            d += int(i)
    print(d)
    break

'''
列表添加 删除 修改 查询
'''
list1 = []
list2 = ["面包"]

list1.append("火腿肠")
print(list1)
list1.append("酸奶")
print(list1)

list2.append("薯条")
print(list2)

list1 += list2 # 列表合并可以用加号
print(list1)

list1.extend(list2) # extend()方法可以将一个列表的元素添加到另一个列表中
print(list1)

'''
删除: pop remove clear
pop(index): 根据索引删除列表中元素, 索引在写的时候要注意不要超出范围, 可以不添加参数, 默认从后往前依次删除
'''
list1 = ["牛奶", "面包", "鸡蛋", "水果", "蔬菜", "饮料", "零食"]
list2 = []
increment = list1.pop()
list2.append(increment)
print(list2)

'''
删除: pop remove clear
remove: 根据元素删除, 如果列表存在多个同名元素, 只删除遇到的第一个元素
'''
list1 = ["牛奶", "面包", "饮料", "鸡蛋", "水果", "蔬菜", "饮料", "零食"]
list1.remove("饮料")
print(list1)
list1.index("饮料",3,7)

'''
删除多个同名元素
'''
list1 = ["牛奶", "面包", "饮料", "饮料", "鸡蛋", "水果", "蔬菜", "饮料", "零食"]
while True:
    if "饮料" in list1:
        list1.remove("饮料")
    else:
        break
print(list1)

'''
删除多个同名元素, 如果同名元素紧挨着, 使用for循环会漏删
'''
list1 = ["牛奶", "面包", "饮料", "饮料", "鸡蛋", "水果", "蔬菜", "饮料", "零食"]
for i in list1[:]: # 这里使用for循环 list1的副本, 因为remove的是list1, 所以副本中的元素没有被remove, for循环可以完整的遍历list1副本中的所有元素, 因此不会有漏删
    if i == "饮料":
        list1.remove(i)
print(list1)

'''
删除: pop remove clear del
clear: 清空列表元素
'''
list1 = [1,2,3,4,5,6]
del list1[3] # del 列表[index], 此方法和使用pop一样
print(list1)

# 用clear清空列表元素, 但列表还在，之后仍可以用append等方法
list1 = [1,2,3,4,5,6]
list1.clear()
list1.append(20)
print(list1)

# 用del删除整个列表, 列表不存在, 之后不能再用append等方法
list1 = [1,2,3,4,5,6]
del list1
list1.append(20)
print(list1)

'''
添加: 列表查找索引, 可以用index方法, 没有find方法
'''
list1 = [1,2,3,4,5,6]
list1.insert(1,9) # insert(索引, 新参数), 在这个索引位置插入新参数, 其他元素向后移动
print(list1)

list1[1] = 8 # 直接在索引1替换成8
print(list1)

'''
修改: 列表[index] = 新参数
'''
location = list1.index(5) # 找出5所在的索引
list1[location] = 10 # 在5所在的索引, 把5替换成10
print(list1)

'''
查找: 
    1. 元素 in/not in 列表  返回bool类型
    2. 列表.index(元素) 返回元素的索引, 如果没有则报错
    3. 列表.count(元素) 返回元素出现的次数, 返回值为0则表示不存在此元素
'''

# 列表可以存储多个数据, list2和list1指向同一个内存地址. list1地址不变, 在原有基础上添加元素, list2也会添加元素. 因为地址相同
list1 = [1,2,3,4,5,6]
list2 = list1
list1.append(7)
print(list1)
print(list2)

list1 = [1,2,3,4,5,6]
list2 = list1
list1.clear()
print(list1)
print(list2)

list1 = [1,2,3,4,5,6]
list2 = list1
del list1
print(list1) # list1不存在
print(list2) # list2存在

# 字符串只存储1个数据, b和a指向同一个内存地址. a赋值变了, 相当于a换了个内存地址, b还是原来的地址. 因此b不等于a
a = 7
b = a
a = 8
print(a)
print(b)

# 字符串只存储1个数据, b和a指向同一个内存地址. 把a赶出这个内存地址, b还在原来的内存地址. 因a不存在, b存在
a = 7 
b = a
del a 
print(a)
print(b)

# 生成8个1-20之间的随机数
# 列表排序

import random
list1 = []
while len(list1) < 8:
    number = random.randint(1,100)
    if number not in list1:
        list1.append(number)
print(list1)

list1.sort() # 正序排列
print(list1)

list1.sort(reverse=True) # 通过reverse参数控制升序还是降序, True是降序, False是升序
print(list1)
list1[0]

list1.reverse() # 调用reverse方法, 没有排序, 列表反转, 并不是按数字大小倒序排序
print(list1)

list1 = [1,2,38,45,5,6]
list2 = sorted(list1) # sorted函数返回一个新列表
print(list1) # 打印原列表, 顺序没变
print(list2) # 打印新列表, 顺序变了
list1.sort() # sort方法是对原列表进行修改
print(list1) # 打印原列表，顺序变了

a = sorted("hello")
print(a)

