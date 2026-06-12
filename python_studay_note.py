#Day01
s='abcdefg'
print(s[0:3])   #从左到右，包含0但不包含3，步长可以省略
print(s[-4:-7:-1])  #从右到左，包含-4但不包含-7，步长为-1,从右往左，步长不能省略
print(s[6:3:-1]) #也表示从右到左，包含6但不包含3，步长为-1,从右往左，步长不能省略
print(s[::])  #步长为1，表示每隔一个字符取一个，如果是取全字符，都可以省略
print(s[::-1]) #步长为-1，表示反向切片，字符串反转
print(s[:6:2]) #从左到右，包含0但不包含6，步长为2,每隔一个字符取一个。从头开始取，开始字符可以省略
print(s[1::2]) #从第二个字符开始取，开始字符不能省略.取到最后1个字符，结束字符可以省略

#Day02
number2=input("Type a number:") #输入的内容是字符串类型
number3=5*int(number2)  #如果要用于计算，需要转换成整数类
print(number3)

#Day03
username="eric"
message=f"Hello {username.title()}, would you like to learn some Python today?" #f-string格式化字符串，使用{}括起来的部分会被替换成变量的值
print(message)
print(username.lower())    #lower()方法将字符串中的所有字符转换为小写
print(username.upper())    #upper()方法将字符串中的所有字符转换为大写
print(username.title())    #title()方法将字符串中的每个单词的首字母大写，其余字母小写，适用于人名等专有名词的格式化

print("Albert Einstein once said, 'A person who nver made a mistake never tried anything new.'") #在字符串中使用单引号时，可以使用双引号将字符串括起来，反之亦然，以避免引号冲突
print("Albert Einstein once said, \"A person who nver made a mistake never tried anything new.\"") #使用转义字符\来在字符串中包含引号

famous_person="Albert Einstein"
message=f"{famous_person} once said, \"A person who nver made a mistake never tried anything new.\""
print(message)

name=" Dai Shiwei "
print(name.lstrip())
print(name.rstrip())   #rstrip()方法用于去除字符串右侧的空白字符
print(name.strip())    #strip()方法用于去除字符串两侧的空白字符

print("Dai\nShiwei\t")  #\n表示换行，\t表示制表符（tab），在字符串中使用转义字符来表示特殊字符或格式

filename="python_notes.txt"
print(filename.removesuffix(".txt"))  #removesuffix()方法用于移除字符串末尾的指定后缀，如果字符串以该后缀结尾，则返回移除后的字符串，否则返回原字符串

2+3
3**2 #**运算符用于求幂，例如3**2的结果是9，因为3的2次幂是9   
3%2 #%运算符用于求两个数相除的余数，例如3%2的结果是1，因为3除以2的商是1，余数是1
print(0.1+0.2)  #由于计算机使用二进制表示小数，某些十进制小数无法精确表示为二进制小数，因此在进行浮点数运算时可能会出现精度问题，导致结果不完全准确，例如0.1+0.2的结果可能会得到0.30000000000000004而不是0.3
1+0.1

my_age=100_000_000_000
print(my_age)  #在Python中，可以使用下划线作为数字的分隔符，以提高数字的可读性，例如100_000_000_000表示一万亿，使用下划线可以更清晰地表示数字的大小，而不会影响数值的计算结果

a,b,c=1,2,3  #同时给多个变量赋值，使用逗号分隔变量和对应的值，左边的变量依次对应右边的值
print(a,b,c)    #输出多个变量的值，使用逗号分隔变量，print函数会在输出时自动添加空格作为分隔符，例如输出a、b、c的值时，会在它们之间添加一个空格，使输出更清晰易读

MAX_HEALTH=100
print(MAX_HEALTH)  #在Python中，常量通常使用全大写字母来命名，以表示它们的值不应该被修改，例如MAX_HEALTH表示最大生命值，使用全大写字母可以提醒程序员这个变量是一个常量，不应该被改变。只是提醒程序员，Python本身并没有真正的常量机制，仍然可以修改MAX_HEALTH的值，但这种命名约定有助于提高代码的可读性和维护性。

2+6
print(2+6)

2*4
print(2*4)

16-8
print(16-8)

24/3
print(24/3)  #在Python中，除法运算符/总是返回一个浮点数，即使两个操作数都是整数，例如24/3的结果是8.0而不是8
24//3
print(24//3)  #在Python中，整除运算符//返回一个整数，即使两个操作数都是整数，例如24//3的结果是8而不是8.0

favorite_number=19
print(f"My favorite number is {favorite_number}")   #使用f-string格式化字符串，将变量favorite_number的值插入到字符串中，输出结果为"My favorite number is 19"

import this #导入Python的内置模块this，输出Python之禅（The Zen of Python），这是Python的设计哲学和指导原则，包含了Python开发者应该遵循的一些核心理念和最佳实践，例如"Beautiful is better than ugly."（优美胜于丑陋）和"Simple is better than complex."（简单胜于复杂）等，这些原则有助于指导Python程序员编写清晰、简洁、易读的代码。

bikes=["trek","giant","camp"]
print(bikes)
print(bikes[0])
print(bikes[0].title())
print(bikes[2].title())
print(bikes[0].title(),bikes[1].title())    #
print(f"My favorite bike is a {bikes[0].title()}")

bikes[0]="specialized"  #更改列表里第1个参数为specialized
print(bikes[1].title())    #列表如果不指定元素，无法用title全显示出来

bikes.append("specialized") #append方法将元素添加到末尾
print(bikes)

#Day04
bicycles=[]
bicycles.append("永久")
bicycles.append("trek") #使用append方法在末尾添加元素
bicycles.insert(1,"giant")  #使用insert方法添加元素
del bicycles[0]    #使用del语句删除元素
print(bicycles)

bicycles=["trek","specialized","camp","giant"]
print(bicycles)
poped_bicycles=bicycles.pop()   #使用pop方法，获取元素并删除，如果括号内不指定参数，默认取最后1个值,再次print，列表中该值已不存在
print(poped_bicycles)
print(bicycles)     #验证已删除最后1个值
print(f"My current bicycle is {poped_bicycles}")
unlike="camp"
bicycles.remove(unlike)
print(bicycles)
print(f"\nI don't like {unlike}")

guest=["dad","mum","brother"]
guest[2]="Uncle"
print(guest)
greeting="Welcome to dinner, "
print(guest)
print(guest.pop())
print(guest)
guest.remove("brother")
guest.append("sister")
print(guest)
guest.insert(0,"Sam")
print(guest)
guest.insert(2,"Oliver")
print(guest)
guest.append("Uncle")
print(guest)
print(f"Welocome to dinner, {guest[0]}. \n{greeting}{guest[1].title()}. \n{greeting}{guest[2].title()}. \n{greeting}{guest[3].title()}. \n{greeting}{guest[4].title()}. \n{greeting}{guest[5].title()}.")
print("Sorry, I can only invite two persons")
not_come_person=guest.pop(5)               #用pop函数提取被删除的参数
print(f"Sorry, {not_come_person}, I cannot invite you")
not_come_person=guest.pop(4)
print(f"Sorry, {not_come_person}, I cannot invite you")
not_come_person=guest.pop(3)
print(f"Sorry, {not_come_person}, I cannot invite you")
not_come_person=guest.pop(2)
print(f"Sorry, {not_come_person}, I cannot invite you")
print(f"{guest[0]}, you're still in the list. \n{guest[1].title()}, you're still in the list.")
print(guest)
len(guest)
del(guest[1])
del(guest[0])
print(guest) 

s="Hello"
print(s[2])
type(s)

a,b=True,False
type(b)

c=None
type(c)

numbers=[-5,0,3,1,19,67,-42]
print(max(numbers))     #max函数取最大值
print(min(numbers))     #min函数取最小值
print(sorted(numbers))
numbers.sort()
print(numbers)

bikes_list=["trek","giant","specialized"]
bikes_list.sort()   #在变量上用sort方法对列表排序，不能直接print，需要单独对list print。可以永久改变列表顺序
print(bikes_list)
print(sorted(bikes_list))   #用sorted函数对列表进行排序，可以直接print，原始list的排序依然存在
print(bikes_list)
print("Here is the bike list")
print(bikes_list)
bikes_list.sort(reverse=True)   #sort方法里填写参数reverse，对列表进行按字母反向排序，永久改变列表顺序
print(bikes_list)
sorted(bikes_list,reverse=True) #用sorted函数，sorted(参数，revers=True)对列表进行反向排序
bikes_list.reverse()    #用reverse方法，反转列表并打印,并不是按字母顺序反向排序
print(bikes_list)
len(bikes_list)

country=["Manchester","Osaka","Xinjiang","Brazil","Egypt"]
print(country)
print(sorted(country))
print(country)
print(sorted(country,reverse=True))
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)
len(country)
len(country[len(country)-1])
country[len(country)-1]
country[-1]
country[4]


pet_list=["Dog","Cat","Bird"]
for pet in pet_list:    #for循环“：”很重要，不要漏了，开区间
    print(f"A {pet.lower()} would make a great pet.\n")
print("Any of these animals would make a great pet")

#Day05
for i in range(6):    #for循环“：”很重要，不要漏了，开区间
    print(i)

numbers=list(range(2,6,2))  #（2，6，2）输出2-5数字中的偶数，后面1个2是步长
print(numbers)

square_list=[]
for value in range(1,11):
    value1=value**2  #使用临时变量value1存储乘方后的数字
    square_list.append(value1)
print(square_list)  #最后的结果输出需要跳出for循环

numbers_list=[1,2,3,4,5,6,7,8,9,0]
min(numbers_list)
max(numbers_list)
sum(numbers_list)

squares=[i**2 for i in range(1,11)] #这里的for循环语句没有冒号
print(squares)

#练习1
for i in range(1,21):
    print(i)

numbers=list(range(1,1000001))  #range函数可以生成数字，list函数把它转换成列表
print(numbers)
min(numbers)
max(numbers)
sum(numbers)

numbers=list(range(1,20,2))
for i in numbers:
    print(i)

value=0
numbers=list(range(1,101))
for i in numbers:
    value=value+i
print(value)

get_numbers=[]
numbers=list(range(3,30,3))
for value in numbers:
    get_numbers.append(value)
print(get_numbers)



numbers=list(range(1,1000001))
for num in numbers:
    print(num)
min(numbers)
max(numbers)
sum(numbers)

cube=[i**3 for i in range(1,11)]
print(cube)

cube=[]
for i in range(1,11):
    i=i**3
    cube.append(i)
print(cube)

numbers=[]
for value in range(1,30):
    if value%3==0:
        numbers.append(value)
print(numbers)

numbers=[value%3==0 for value in range(1,30)]   #value%3==0,是判断条件返回的是bool
print(numbers)  #打印出来的是True和False

players=["a","b","c","d","e"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:]) #如果结束字符没指定，就默认往右抓取
print(players[-3:-5:-1])

print("Here is the player list:")
for player in players[:3]:
    print(player.title())

copy_list=players[:]    #复制players列表，成为一张新的列表，与players同时存在
print(copy_list)
players.append("f")
print(players)
copy_list.append("l")
print(copy_list)

second_list=players #这是对变量重新命名，并没有复制一张新的表，后台仍然只有1张表
players.append("v")

# 对second list增加p，因此second list和players都是同一张表，增加v就被增加p给覆盖了
second_list.append("p") 
print(second_list)
print(players)

players=["a","b","c","d","e"]
print("Ths first 3 items in the list are")
print(players[0:3])
print("The 3 items form the middle of the list are")
print(players[1:4])
print("The last 3 items in the list are")
print(players[2:])

my_pizza=["a","b","c"]
friend_pizzas=my_pizza[:]
my_pizza.append("d")
friend_pizzas.append("e")
print(my_pizza)
print(friend_pizzas)

print("My favorite pizzas are")
for pizzas in my_pizza[0:]:
    print(pizzas)
print("My friend's favorite pizzas are")
for friend_pizza in friend_pizzas[0:]:
    print(friend_pizza)

dimension=(50,100)  #元组
print(dimension[0])
for i in dimension:
    print(i)
modified_dimension=(400,200)
print(modified_dimension)

food_list=("a","b","c","d","e")
for food in food_list:
    print(food)
new_food_list=("f","b","c","x","e")
for food in new_food_list:
    print(food)

cars=["audi","bmw","subaru","toyota"]
for car in cars:
    if car=="bmw": # == 表示等于
        print(car.upper())
    else:
        print(car.title())

car="Audi"
car=="audi" # 大小写不同，值不同
car.lower()=="audi"

my_car="byd"
if my_car!="audi":
    print("Please buy Audi")

age_0=22
age_1=18
(age_0>=21) and (age_1>=21)
(age_0>=21) and (age_1>=18)
(age_0>=21) or (age_1>=21)

my_car=["audi","bmw","subaru","toyota"]
"audi" in my_car
"tesla" in my_car
car="tesla"
if car not in my_car:
    print("I want it!")

car="tesla"
print(car=="tesla")

first="Audi"
second="audi"
first==second

age=30
if age<4:
    price=0
elif age<18:    # elif语句仅适用于1个条件满足的情况，在遇到通过的条件后，就会跳过后面的测试
    price=10
else:           # 因此elif语句要从最小的情况开始
    price=50
print(f"Please buy a ticket, the price is ${price}")

# alien_color="red"
# if alien_color=="green":
#     print("You got 5 points")

# alien_color="red"
# if alien_color=="green":
#     print("You got 5 points")
# else:
#     print("You got 10 points")

alien_color="red"
if  alien_color=="green":
    print("You got 5 points")
elif    alien_color=="yellow":
    print("You got 10 points")
else:
    print("You got 15 points")

age=65
if  age<2:
    print("It's baby")
elif    age<4:
    print("You're a infant")
elif    age<13:
    print("You're a child")
elif    age<18:
    print("You're a teenage")
elif    age<65:
    print("You're a adult")
elif    age>=65:
    print("You're a old man")

available_list=["audi","bmw","subaru","toyota"]
requested_list=["audi","bmw","byd","tesla"]
for car in requested_list:
    if car in available_list:
        print(f"We have it, adding {car}")
    else: print(f"Sorry, we don't have {car}")
print("This is your bill")

user_list=["admin","Apple","Tom","Peter","John"]
del(user_list[:])
for username in user_list:
    if  username=="admin":
        print(f"Hello {username}, would yuo like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users")

# current_users=["david","apple","Tom","peter","John"]
# new_users=["David","Frank","Wayne","Peter","Mike"]
# current_users_lower=[]
# for user in current_users:
#     user=user.lower()
#     current_users_lower.append(user)
# print(current_users_lower)
# for user in new_users:
#     if user.lower() in current_users_lower:
#         print(f"{user}已经存在，请输入别的用户名")
#     else:   print(f"{user}未被使用")

user=input("Type your name:")
current_users=["david","apple","Tom","peter","John"]
current_users_lower=[user.lower() for user in current_users]    #如果用现有表推导新的表，可以用列表推导式
print(current_users_lower)
if  user.lower() in current_users_lower:
    print(f"{user}已经存在，请输入别的用户名")
else:
    print(f"{user}未被使用")

numbers=list(range(1,10))   #如果是数字列表，可以用list函数+range函数生成列表
for number in numbers:
    if number == numbers[0]:
        print("1st")
    elif number == numbers[1]:
        print("2nd")
    elif number == numbers[2]:
        print("3rd")
    else:
        print(f"{number}th")

#Day06
alien_0 = {("color", 23):"green"}
alien_0["points"] = 5
print(alien_0)
alien_0["points"] = 25
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
alien_0["color"] = "yellow"
print(alien_0)
del alien_0['color']
print(alien_0)
alien_0["speed"] = "fast"
print(alien_0)
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:   x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"x new position is {alien_0['x_position']}")
alien_0[("color",24)] = "green"     #字典中键不能重复，值可以重复。如遇到重复的键名称，例如同名同姓，可以用元组来表示键
print(alien_0)

favorite_color = alien_0[("color", 23)]
favorite_thing = alien_0.keys() #favorite_thing[1] 用字典读取键后，不能用键索引来读取指定的键
print(favorite_thing)
print(f"My favorite color is {favorite_color}")

#练习6.1
person = {"first name":"诗伟","last name":"戴","age": 35,"city":"上海"}
print(f"{person['last name']}{person['first name']},年龄:{str(person['age'])}岁,生活在{person['city']}.")   #fstring外部使用双引号，内部使用单引号，字符串不能和数字类型连接，所以要把数字类型用str()转换成字符再连接

#练习6.2
favorite_number = {"jason":6,"sam":7,"peter":10,"oliver":2,"tom":5}
print(f"Jason's favorite number is {favorite_number['jason']}.")
print(f"Sam's favorite number is {favorite_number['sam']}.")
print(f"Peter's favorite number is {favorite_number['peter']}.")
print(f"Tom's favorite number is {favorite_number['tom']}.")
print(f"Oliver's favorite number is {favorite_number['oliver']}.")

#练习6.3
vocabulary = {"for":"for循环","print":"打印","list":"列表"}
word = "for"
print(f"\n{word.title()}: {vocabulary[word]}")
for word,definition in vocabulary.items():
    print(f"{word.title()}: {definition}") 

#练习6.5
rivers = {"nile":"egypt","Yangtze river":"china"}
for river, country in rivers.items():   #这里的river.items不要漏了，否则会出现错误
    print(f"The{river.title()} runs through {country.title()}")

#练习6.6
favorite_number = {"jason":6,"sam":7,"peter":10,"oliver":2,"tom":5}
investigator = ["jason","oliver","david"]
for name in investigator:
    if name in favorite_number.keys():
        print(f"Thank you for survey, {name.title()}")
    else:
        print(f"Invite you to do a survey, {name.title()}")

#练习6.7
person1 = {"first name":"诗伟","last name":"戴","age": 35,"city":"上海"}
person2 = {"first name":"韵黛","last name":"曹","age": 34,"city":"上海"}
people = [person1, person2]
for person in people:
    print(
        f"姓名:{person['last name']}{person['first name']},"    #使用多个f string来换行，保持代码长度
        f"年龄:{str(person['age'])}岁,"
        f"居住地:{person['city']}."
        )

#练习6.8
pets=[]
pet = {"type":"a","owner":"ruby"}
pets.append(pet)
print(pets)
pet = {"type":"b","owner":"sam"}
pets.append(pet)
print(pets)
for pet in pets:
    print(
        f"Pet type is {pet['type']},"
        f"Owner is {pet['owner']}"
    )
#练习6.9
favorite_places = {
    "sam":["a","b","c"],
    "oliver":["d"],
    "John":["x","f"]
    }
for name,places in favorite_places.items():
    if len(places)==1:
        print(f"{name.title()}'s favorite place is")
    else:
        print(f"{name.title()}'s favorite place are")
    for place in places:
        print(place.upper())

#练习6.10
favorite_number = {"jason":[6,8,9],"sam":[7,19],"peter":[10],"oliver":[2,6,9],"tom":[5,88]}
for name,numbers in favorite_number.items():
    print(f"{name.title()}'s favorite number is")
    for number in numbers:
        print(number)
#练习6.11
cities = {}
cities["shanghai"] = {"country":"china","fact":"modern","population":"60m"}
cities["paris"] = {"country":"france","fact":"romantic","population":"10m"}
for city,city_info in cities.items():
    print(city.title())
    country = city_info["country"]  #使用变量把嵌套字典信息表示出来，才能用title方法
    fact = city_info["fact"]
    population = city_info["population"]
    print(f"\nCountry: {country.title()}")
    print(f"Fact: {fact.title()}")
    print(f"Population: {population.title()}\n")

cities = {
    "shanghai":{
        "country":"china",
        "fact":"modern",
        "population":"60m"}
        }

#Day07
prompt = "If you share name"
prompt += "\nWhat's your name?: "
name = input(prompt)

print(f"\nHello {name}!")

age = input("How old are you? ")
age=int(age)
age >18

#练习7.1
car = input("what kind of car do you wanna rent? ")
print(f"Let me see if I can find you a {car.title()}")

#练习7.2
number_of_people = int(input("How many people? "))
if number_of_people > 8:
    print(f"There is no free table.")
else:
    print(f"We have free tables.")

#While 循环
number = 0
while number in range(5):
    print(number)
    number += 1

prompt = "\nTell me something."
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != "quit":
        message = input(prompt)
        if message != "quit":
            continue
        print(message)

prompt = "\nTell me something."
prompt += "\nEnter 'quit' to end the program: "

while True:
    message = input(prompt)
    if message == "quit":   #当有一个判断条件时，break语句更简练
        break
    else:
        print(message)

current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number %2 ==0:   #continue语句适用于有2个判断条件，并用反向逻辑求值。例如：我要取奇数
        continue
    print(current_number)

#练习7.4
while message != "quit":
    message = input("请输入你想要的配料： ")
    print(f"你要的配料是 {message}")

#练习8.9
def show_message(message):
    for message in messages:
        print(message)

messages = ["你好","你吃了吗？"]
show_message(messages)

def show_message(message):
    print("Original messages:")
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    print("Sending message")
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

messages = ["你好","你吃了吗？"]
sent_messages = []
show_message(messages)
send_messages(messages,sent_messages)
print(messages)
print(sent_messages)


messages = ["你好","你吃了吗？"]
sent_messages = []
def show_message(messages):
    for message in messages:
        print(message)
def send_message(messages,sent_messages):
    print("Sending message")
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

print("Original message:")
show_message(messages)
send_message(messages[:],sent_messages)
print("Final result")
print(messages)
print(sent_messages)

def making_pizza(*toppings):
    print("Making your pizza with these toppings:")
    for topping in toppings:
        print(topping)
toppings = []
while True:
    topping = input("Enter the topping: ")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
making_pizza(toppings)      #现在toppings是个列表，Python会把这个列表当成1个元素，因此打印出来是个列表
making_pizza(*toppings)     #解决方案：函数在调用时加“*”解包，这样也可以逐个打印

def making_pizza(*toppings):
    print("Making your pizza with these toppings:")
    for topping in toppings:
        print(topping)
making_pizza("cheese","meat")   #输入的参数是2个元素，Python认为是2个元素，因此会逐个打印
