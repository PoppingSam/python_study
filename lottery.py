# 模拟1次彩票抽奖
from random import choice

# 生成1个彩票池，带有数字和字母
lottery = [1, 8, 25, 69, 11, 7, 54, 30, 87, 4, "a", "e", "w", "m", "c"]

# 最大尝试次数赋值，避免长时间运行
max_try = 10000


# 定义一个随机抽4个号码的函数
def make_my_ticket():
    while len(my_ticket) < 4:
        lottery_number = choice(lottery)
        if lottery_number not in my_ticket:
            my_ticket.append(lottery_number)
    return my_ticket


# ==== 主执行代码 ====
winner_ticket = []

# 当ticket小于4个数字时循环抽取，抽取1次就加到ticket里
while len(winner_ticket) < 4:
    lottery_number = choice(lottery)
    if lottery_number not in winner_ticket:
        winner_ticket.append(lottery_number)

# 打印消息
print(f"只要你的彩票上是这4个数字或字母就中奖了!\n"
      f"中奖号码是: "
      )

# 1个号码为1行
for lottery_number in winner_ticket:
    print(lottery_number)

my_ticket = []
play = 0

# 循环抽奖直至抽中或达到最大次数
while True:
    if my_ticket != winner_ticket:
        play += 1
        del my_ticket[:]
        my_ticket = make_my_ticket()
        print(f"我的号码是{my_ticket},很遗憾没有中奖,您已尝试{play}次")

        if play == max_try:
            break
    else:
        print(f"恭喜您中奖了！"
              f"中奖号码是：{winner_ticket}"
              f"你的号码是：{my_ticket}"
              f"共尝试了{play}次"
        )
        break