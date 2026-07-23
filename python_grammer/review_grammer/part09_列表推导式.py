'''
列表推导式: 最终得到一个列表
格式1:[i for i in 可迭代的]
格式2:[i for i in 可迭代的 if 条件]
格式3:[结果1 if 条件 else 结果2 for 变量 in 可迭代的]
格式4:[结果1 if 条件1 else 结果2 for 变量 in 可迭代的 if 条件2]
'''

list1 = [i for i in range(1,21)]
print(list1)

# 1-100之间的偶数, 存放到列表
list1 = [i for i in range(1,101) if i % 2 == 0]
print(list1)

list2 = ["62","hello", "100", "lucky","high"]
list3 = [i for i in list2 if i.isalpha()]
print(list3)

list2 = ["62","hello", "100", "lucky","high"]
list4 = [word.title() if word.startswith("h") else word.upper() for word in list2 if word.isalpha()]
print(list4)

a = [x for x in range(1,101)] #1,2,3,4,5,6,7,8,9
b = [a[i:i+3] for i in range(0, len(a),3)]
print(b)