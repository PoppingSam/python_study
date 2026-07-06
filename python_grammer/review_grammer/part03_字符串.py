print("hahahahahaha")

# \n 换行
print("haha\nhahahaha")

# \t tab缩进
print("haha\thahahaha")

# \\ 代表1个\
print("haha\\hahahaha")

# \' 代表单引号
print("haha\'haha\'haha")

# \" 代表双引号
print("haha\"hahahaha")

# 不想转义，前面加r,如果不加r,\n会换行
print(r"nana\nananana")

# 变量2 = 变量1时, 两者相同，is 返回 true
# 变量内容一样时，两者相同，is 返回 true
s1 = "hello"

s2 = s1

s3 = "hello"

print(id(s1),id(s2),id(s3))
print(s1 is s2)
print(s1 is s3)
print(s2 is s3)

s1 = "world"
print(s1 is s2)
print(s1 is s3)
print(s2 is s3)

# 字符串截取,索引: index
# 从左往右从0开始，0~len(s)-1,从右往左从-1开始, -len(s)~-1
s1 = "abcdefg"
print(s1[4])
print(s1[0])
print(s1[-1],s1[5])
print(len(s1))

# 切片: 字符串, 列表
# 字符串变量[start:end:step] 从左往右step可省略，从右往左step不能省略
print(s1[4:0:-1])
print(s1[:5]) # 从0开始,0可以省略
print(s1[-3:])
print(s1[:]) # 从头到尾
print(s1[1:-1]) # 不要两头，取中间
print(s1[:-1:2])
print(s1[1:-1:2])
print(s1[::4])
print(s1[-3::-4])

'''
https://zhuanlan.zhihu.com/p/398633846
'''
# find:从左往右查找，只要遇到1个符合要求则返回位置，如果没有找到符合要求的则返回-1
# index, rfind, rindex

path = "https://zhuanlan.zhihu.com/p/398633846.gif"

i = path.find('p/')
print(i)

image_name = path[i+2:]
print(image_name)

# rfind: 从右往左查找，只要遇到1个符合要求则返回位置，如果没有找到符合要求的则返回-1
i = path.rfind('.')
image_name = path[i+1:]
print(image_name)

# 查找字符串中有几个点, 使用count
i = path.count(".")
print(i)

# index与find区别: index也是表示查找，如果找不到会报错
i = path.index('#')

i = path.find('zhihu') # 返回查找内容的第一个字符的位置
print(i)

'''
startswith, endswith, isalpha, isdigit, isalnum, isspace
'''
s = "e398sd63v3846.gif"
result = s.startswith("e3")
print(result)
result = s.endswith("mp4")
print(result)

'''
模拟上传文件,扩展名是jpg, gif, png, 文件名需要是6位, 如不满足6位, 随机生成1个6位名字
并打印成功上传文件名
'''

import random

file = input("请输入上传的文件名称")

# 判断文件名位置
dot_index = file.find(".")
list_range = ("QWERTYUIOPASDFGHJKLZXCVBNM"
        "qwertyuiopasdfghjklzxcvbnm0123456789")

# 检查文件类型是否是png, jpg, gif
if file.endswith("png") or file.endswith("jpg") or file.endswith("gif"):

# 检查文件名是否是6位，如不满足6位则随机生成1个6位名字
    if len(file[:dot_index]) < 6:
        file_name = ""
        for i in range(6):
            index = random.randint(0, len(list_range)-1)
            file_name += list_range[index]
        file = f"{file_name}{file[dot_index:]}"
        print(f"成功上传{file}")
# 条件全满足
    else:
        print(f"成功上传{file}")
# 返回文件类型不正确
else:
    print("上传失败,请检查文件类型")

#=====================================
'''
变量必须是字符串类型
isalpha: 都是字母组成
isdigit: 都是数字组成
isalnum: 由字母和数字组成
isspace: 都是空白,只要有内容就返回false
isupper: 都是大写
islower: 都是小写
'''
s = "Abde213"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isupper())
print(s.islower())

s = "124 gn"
print(s.isspace())

# replace(old, new, count): 默认全部替换，也可以通过count指定次数
s = "a是个大笨蛋, b是个大大笨蛋"
result = s.replace("笨蛋", "聪明", 1) # 数字代表替换几次
print(result)

# 如果要同时替换2个词，需要用正则表达式或循环+列表

# split("分隔符"，count), 返回的结果是1个列表，count指定次数
# 同理rsplit
s = "a b c"
result = s.split(" ",1)
print(result) # ['a', 'b c']

# splitlines: 按行分割, 返回的结果是1个列表
s = '''床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''
result = s.splitlines()
print(result)

# partition
s = "a b c"
result = s.partition(" ")
print(result) # ('a', ' ', 'b c')

# 大小写转换
s = "hello World"
result = s.title()
print(result)
result = s.upper()
print(result)
result = s.lower()
print(result)
result = s.capitalize() # 第一个单词的首字母变大写, Hello world
print(result)

# 空格处理
username = " admin      "
print(username)
len(username)
result = username.strip() # 去除两侧空格
print(result)
len(result)
result = username.lstrip() # 去除左侧空格
print(result)
len(result)
result = username.rstrip() # 去除右侧空格
print(result)
len(result)

# ljust, rjust, center 添加空格，控制对齐
s = "hello World"
result = s.rjust(30) # 右对齐
print(result)
result = s.center(30) # 居中
print(result)
result = s.ljust(30) # 左对齐
print(result)

# join 在abc后面分别增加m，打印出来ambmcm 
s = "m"
result = s.join("abc")
print(result)

# 字符串格式化
name = "sam"
age = 18
result = "帅哥{}今年{}岁".format(name, age)
print(result)

result = "帅哥{0}今年{1}岁, 我也{1}岁".format(name, age)
print(result)

result = f"帅哥{name}今年{age}岁, 我也{age}岁"
print(result)

result = "帅哥{name}今年{age}岁, 我也{age}岁".format(name = "sam", age = 18)
print(result)




























