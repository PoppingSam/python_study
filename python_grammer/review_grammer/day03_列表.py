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
删除: pop remove clear
clear:
'''