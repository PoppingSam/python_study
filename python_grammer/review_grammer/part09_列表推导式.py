'''
列表推导式: 最终得到一个列表
格式1:[i for i in 可迭代的]
格式2:[i for i in 可迭代的 if 条件]
'''

list1 = [i for i in range(1,21)]
print(list1)

# 1-100之间的偶数, 存放到列表
list1 = [i for i in range(1,101) if i % 2 == 0]
print(list1)