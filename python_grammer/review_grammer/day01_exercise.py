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











