""" 用Python设计第一个游戏 """
""" 猜数字游戏 """

import random

answer = random.randint(1,100)
counts = 3
while counts > 0:
    temp = input("不妨猜一下我现在心里想的是哪个数字：")
    guess = int(temp)

    if guess == answer:
        print("你是我心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励！")
        break
    else:
        if guess < answer:
            print("猜小了")
        else:
            print("猜大了")
        counts = counts - 1
        
    
print("游戏结束，不玩啦^_^")
print("我心里想的是：" , answer)
