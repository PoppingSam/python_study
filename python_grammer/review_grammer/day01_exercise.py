'''
1.订单金额计算
已知某医疗器械单价为 128.5 元，采购数量为 80 件。
编写程序计算：
订单总金额
如果订单总金额大于或等于 10000 元，输出 True
否则输出 False
'''
unit_price = 128.5
purchase_qty = 80
total_value = unit_price * purchase_qty
print(total_value)
print(total_value >= 10000)

#=======================
'''
2. 包装箱数量计算
某产品需要发货 257 件，每箱最多装 24 件。
编写程序计算：
可以装满多少箱
最后一箱剩余多少件
是否需要额外增加一个包装箱
要求使用整除、取余和比较运算符。
'''
ship_qty = 257
max_unit_qty = 24
box_qty = ship_qty // max_unit_qty
last_box_qty = ship_qty % max_unit_qty

print(box_qty, last_box_qty)
if last_box_qty:
    print("需要额外再加1箱")

#=================================
'''
3. 库存状态判断
已知：
inventory = 120
safety_stock = 50
monthly_demand = 90
编写程序判断：
当前库存是否高于安全库存
当前库存是否能够同时满足月度需求和安全库存要求
将两个判断结果分别打印出来
'''
inventory = 120
safety_stock = 50
monthly_demand = 90
print(inventory > safety_stock)
print(inventory >= safety_stock + monthly_demand)

#===========================================
'''
4. 折扣价格计算
某产品原价为 850 元。如果采购数量大于或等于 100 件，可以享受 8% 的折扣。
编写程序：
根据采购数量判断是否满足折扣条件
计算折扣后的单价
计算订单总金额
'''
unit_price = 850
purchase_qty = int(input("需要采购: "))
if purchase_qty >= 100:
    unit_price *= 0.92

print(unit_price, unit_price*purchase_qty)

#=========================================
'''
5. 产品编码检查
已知有效产品编号如下：
valid_codes = ["MD1001", "MD1002", "MD1003", "MD1004"]
编写程序判断：
"MD1003" 是否为有效产品编号
"MD2001" 是否不在有效产品编号列表中
将两个判断结果打印出来
'''
valid_codes = ["MD1001", "MD1002", "MD1003", "MD1004"]
print("MD1003" in valid_codes)
print("MD2001" not in valid_codes)

#=========================================
'''
1. 医疗器械缺货风险判断
某医疗器械的供应链数据如下：
inventory = 500
in_transit = 200
forecast_demand = 800
safety_stock = 100
请编写程序：
计算预计可用库存。
判断预计可用库存能否同时覆盖预测需求和安全库存。
计算预计库存缺口。
输出是否存在缺货风险。
要求使用算术、比较和逻辑运算符。
'''
inventory = 500
in_transit = 200
forecast_demand = 800
safety_stock = 100

atp_inventory = inventory + in_transit
print(atp_inventory)
print(atp_inventory >= forecast_demand and atp_inventory - forecast_demand >= safety_stock)

inventory_gap = forecast_demand + safety_stock - inventory - in_transit

if inventory_gap > 0:
    print("有缺货风险", inventory_gap)
else:
    print("无缺货风险")

#=========================================
'''
2. 供应商交付判断
供应商承诺交付数量为 1000 件，实际交付数量为 950 件，承诺交期为 15 天，实际交期为 18 天。
请编写程序判断：
数量是否完全交付。
是否按时交付。
是否同时满足数量和交期要求。
是否至少满足其中一项要求。
'''
promise_qty = 1000
actual_delivery = 950
promise_lead_time = 15
actual_lead_time = 18

print(actual_delivery >= promise_qty)
print(actual_lead_time <= promise_lead_time)
print(actual_delivery >= promise_qty and actual_lead_time <= promise_lead_time)
print(actual_delivery >= promise_qty or actual_lead_time <= promise_lead_time)

#=========================================
'''
3. 产品效期风险判断
某批医疗器械数据如下：
remaining_shelf_life = 5
minimum_shelf_life = 6
inventory = 300
monthly_demand = 40
请编写程序：
判断剩余效期是否达到最低要求。
计算按照当前月需求，需要多少个月才能消耗完库存。
判断产品是否可能在库存消耗完之前出现效期风险。
输出最终风险判断结果。
'''
remaining_shelf_life = 5
minimum_shelf_life = 6
inventory = 300
monthly_demand = 40

print(remaining_shelf_life >= minimum_shelf_life)
print(inventory / monthly_demand)

inventory_consumption_month = inventory / monthly_demand

if remaining_shelf_life - inventory_consumption_month < minimum_shelf_life:
    print("有效期风险")
else:
    print("无效期风险")

#=======================================
'''
4. 采购建议数量计算
某产品数据如下：
forecast_demand = 1200
inventory = 450
in_transit = 300
safety_stock = 200
moq = 100
请编写程序：
计算采购缺口。
判断采购缺口是否大于 0。
根据最小订购量 moq，计算需要采购多少个完整批次。
计算最终建议采购数量。
要求最终采购数量是 moq 的整数倍。
'''
forecast_demand = 1200
inventory = 450
in_transit = 300
safety_stock = 200
moq = 100

purchase_gap = forecast_demand + safety_stock - inventory - in_transit
print(purchase_gap)
print(purchase_gap > 0)

completed_batch_qty = purchase_gap // moq
print(completed_batch_qty)

if purchase_gap <= 0:
    purchase_qty = 0
    print(purchase_qty)

elif purchase_gap % moq > 0:
    completed_batch_qty += 1
    purchase_qty = moq * completed_batch_qty
    print(purchase_qty)
else:
    purchase_qty = moq * completed_batch_qty
    print(purchase_qty)

#=======================================
'''
5. S&OP异常预警
某产品本月数据如下：
forecast = 1000
actual_sales = 1300
inventory = 150
safety_stock = 200
supplier_delay = True
请编写程序判断：
实际销量是否高于预测。
当前库存是否低于安全库存。
供应商是否发生延期。
当以上三个条件同时成立时，输出高风险预警。
当三个条件中至少有两个成立时，输出一般风险预警。
'''
forecast = 1000
actual_sales = 1300
inventory = 150
safety_stock = 200
supplier_delay = True

print(actual_sales > forecast)
print(inventory < safety_stock)
print(supplier_delay)

condition1 = actual_sales > forecast
condition2 = inventory < safety_stock
condition3 = supplier_delay

if condition1 + condition2 + condition3 == 3:
    print("存在供应高风险")
elif condition1 + condition2 + condition3 >= 2:
    print("一般供应高风险")

#=======================================
'''
输入价格个数量，计算购买总金额
'''
total = 0
while True:
    price = float(input("请输入价格"))
    qty = int(input("请输入数量"))
    total += price * qty
    answer = input("是否继续添加商品？按'q'退出：")
    if answer == 'q':
        break
print(f"您购买的总金额是：{total}元")


#=======================================
'''
产生一个随机数，可以猜多次，直到猜中为止. 猜错了提示猜大还是猜小
'''
import random

number = random.randint(1,50)
count = 0
while True:
    guess = int(input("从1-50之间猜1个数字: "))
    count += 1

    if guess == number:
        if count == 1:
            print("运气真好，去买彩票吧！")
        elif 1 < count <= 5:
            print("猜中了，运气不错！")
        else:
            print("猜中了，运气一般！")
        break
    elif guess > number:
        print("猜大了")
    else:
        print("猜小了")

#=======================================
'''
九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        result = i * j
        print(f"{i} x {j} = {result:<3}", end = "  ") # 用end+空格实现不换行
    print() # 空打印，只干一件事——换行

#=======================================
'''
1-50累计和，用for 循环
'''
j = 0
for i in range(1,51):
    j += i
print(j)

#=======================================
'''
输入用户名和密码,提示输入3次错误,账户被锁定
'''
for count in range(3):
    username = input("输入用户名")
    password = input("输入密码")

    if username == "admin" and password == "1234":
        print("登录成功")
        break
    print("用户名或密码有误")
else:
    print("账户被锁定")

#=======================================
'''
掷骰子
两个: 1-6
1. 玩游戏要有金币，没金币不能玩游戏
2. 玩游戏赠金币1枚, 充值获取金币
3. 10元的倍数,得20个金币 
4. 玩游戏消耗5个金币
5. 猜大小：猜对 鼓励金币2枚,猜错没有奖励 点数相加超出6点以上认为是大,否则是小
6 游戏结束:1.主动退出 2. 没有金币退出
7 只要退出则打印金币数，共完了几局
'''
import random

# 建立初始值，局数和金币数为0
count = 0
gold_coins = 0

# 玩游戏前需充值，金币等于充值金额的2倍
print("玩游戏前请充值, 需充值10元的倍数, 充值10元即获得20枚金币")

while True:
    charge = int(input("请输入充值金额: "))
    if charge % 10 != 0:
        print("充值错误,请充值10元的倍数")
    else:
        gold_coins += charge * 2
        print(f"您的金币数是{gold_coins}")
        break

# 当金币数大于5的时候进入循环
while gold_coins >= 5 :

# 两个骰子点数相加
    result = random.randint(1,6) + random.randint(1,6)

# 按q退出，1表示大，2表示小. 
    guess = input("猜大小(1表示大/2表示小),按'q'退出: ")
    if guess == "q":
        break
    elif guess not in ("1", "2"):
        continue   

# 玩一局，赠送1枚金币且消耗5枚金币 
    count += 1
    gold_coins += 1
    gold_coins -= 5

# 点数大于6时为大，小于等于6时为小，猜对加2枚金币
    if (guess == "1" and result > 6) or (guess == "2" and result <= 6):
        gold_coins += 2
        print(f"骰子点数: {result}点, 恭喜你,获得2枚金币, 您还剩{gold_coins}枚金币")
    else:
        print(f"骰子点数: {result}点, 真遗憾, 猜错了, 您还剩{gold_coins}枚金币")

# 结束打印结果
print(f"您一共玩了{count}局, 总计{gold_coins}枚金币")

#=======================================
'''
打印三角形
'''
for i in range(1,6):
    print("*" * i)
# ==========================
i = 1
while i <= 5:  # 外层控制行数
    m = 0
    while m < i: # 内层控制打印
        print("*", end="") # print 默认自动换行，如果不想换行可以加end = ""
        m += 1 
    i += 1
    print()


'''
打印矩形
'''
i = 1
while i <= 4:
    print("*" * 4)
    i += 1

'''
用户名: admin123 
手机号: 15811119999
密码: 200325

用户名或者手机号码登录+密码
用户名：全部小写, 首字母不能是数字, 长度必须6位以上
手机号码: 纯数字 长度11
密码必须是6位数字

以上符合条件, 则进入下层验证
判断用户名+密码 是否正确, 则成功, 否则登录失败
'''
flag = True
while flag:
    username = input("请输入你的用户名/手机号: ")
    if (username.islower() and not username[0].isdigit() and len(username) > 6) or (username.isdigit() and len(username) == 11):
        while True:
            password = input("请输入你的密码: ")
            if password.isdigit() and len(password) == 6:
                if (username == "admin123" or username == "15811119999") and password == "200325":
                    print("登录成功")
                    flag = False
                    break
                else:
                    print("用户名或密码输入错误")
                    break
            else:
                print("密码必须是6位数字")
    else:
        print("用户名格式错误")

'''
模拟论坛
'''

msg = input("发表一句话:")
print("="*30)
print("以下为回复内容")
while True:
    username = input("用户名:")
    comment = input("请输入你的回复:").strip()
    if len(comment) != 0:
        if len(comment) <= 20:
            print(f"\t{username}回复:\n\t{comment}")
            break
        else:
            print("回复字数超过20个字")
    else:
        print("回复内容不能为空, 请重新输入")

'''
买多件商品
商品名,价格,数量
'''

list1 = [] # 购物车
total_qty = 0
total_amount = 0
flag = True
while flag:
    # 添加商品
    product = input("请输入商品名称: ")
    price = input("请输入价格:")
    qty = input("请输入数量:")
    goods = [product, price, qty]
    # 将商品添加到购物车中
    list1.append(goods)

    answer = input("是否需要继续添加, 按q/Q退出:")
    if answer.lower() == "q":
        flag = False

    # 遍历list1
for goods in list1:
    print(f"{goods[0]}\t{float(goods[1])}\t{int(goods[2])}")
    total_qty += int(goods[2])
    total_amount += float(goods[1]) * int(goods[2])
print(f"您一共购买了{total_qty}件, 消费的总金额共计{total_amount}元")