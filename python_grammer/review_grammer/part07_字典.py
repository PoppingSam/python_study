'''
字典: 使用{}, 存储的是键值对 Key : Value. 字段中的key不能重复, Value可以重复
添加元素:
字典[key] = value
'''
dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
print(dict1["王力宏"])

# 修改元素
dict1["林俊杰"] = 85
print(dict1)

# 查找元素
dict2 = {
    "王力宏": {"语文": 99, "数学": 77, "英语": 66}, 
    "周杰伦": {"语文": 88, "数学": 65, "英语": 42}, 
    "林俊杰": {"语文": 68, "数学": 84, "英语": 75}
}
print(dict2)
print(dict2["周杰伦"]["数学"])

'''
练习:
book = {}
书名 价格 作者 出版社
促销: 价格8折
打印字典中的内容
'''
book = {}
book["书名"] = "Python"
book["价格"] = 50
book["作者"] = "Sam"
book["出版社"] = "人民出版社"
book["价格"] *= 0.8
print(book)

# 字典删除
book = {'书名': 'Python', '价格': 40.0, '作者': 'Sam', '出版社': '人民出版社'}

book.clear() # 清空
print(book)

book.pop("出版社") # pop根据key删除键值对
print(book)

book = {'书名': 'Python', '价格': 40.0, '作者': 'Sam', '出版社': '人民出版社'}
r = book.popitem() # popitem 返回元组, 元组里包含键和值, 默认从后往前删除
print(r)
print(book)

del book["作者"] # del 类似于pop
print(book)








