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

# 删除每一本的出版社
books = [
    {'书名': 'Python', '价格': 40.0, '作者': 'Sam', '出版社': '人民出版社'},
    {'书名': 'C++', '价格': 30.0, '作者': 'Sam', '出版社': '邮电出版社'}
    ]

for book in books:
    book.pop("出版社")
print(books)

'''
遍历和查询:
list.index() list.count() in
dict.get(key)
dict[key]
区别在于: get(key) 通过get获取不存在的key,返回None, 不会报错.同时可以设置默认值

'''
# 根据key获取value的值
book = {'书名': 'Python', '价格': 40.0, '作者': 'Sam', '出版社': '人民出版社'}
value = book.get("书名2", "默认值") # 通过get获取不存在的key,返回None, 不会报错.同时可以设置默认值
print(value)

# 如果使用for..in 直接遍历字典，取出的是字段的key
book = {'书名': 'Python', '价格': 40.0, '作者': 'Sam', '出版社': '人民出版社'}
for i in book:
    print(i)

book.values()
# dict.values 获取字典中所有的value值, 存放到一个列表
for v in book.values():
    print(v)

# dict.keys 获取字典中所有的key值, 存放到一个列表
for k in book.keys():
    print(k)

# dict.items 获取字段中的键值对，存放到一个列表, 返回每一个元组
# dict.items [(key, value),().....]
book.items()
for m in book.items():
    print(m) # 返回1个元组(key,value)

for k, v in book.items(): # 把key和value拆分
    print(k,v)
    print(k)
    print(v)

# setdefault 只能用于添加
book.setdefault("渠道", "电商") 
print(book)

# update 将2个字典合并
dict1 = {"a":10}
book.update(dict1)
print(book)

# fromkeys调用的是类, 一定要用dict
result = dict.fromkeys(["c", "d"])
print(result) # 创建1个新字典, key是c,d
result = dict.fromkeys(["c", "d"],20)
print(result) # 通过设置参数, 将参数赋值给key

