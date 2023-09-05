#循环100以内求和
"""
i = 0
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
print(f"100以内的求和为：{n}")
"""

#while猜数字
"""
import random # 随机数
num = random.randint(1,100)
flag = True
i=0
while flag:
    guess = int(input("请输入你猜测的数字："))
    if guess == num:
        print("恭喜你回答正确！")
        flag = False
    else:
        if guess < num:
            print("比实际数字小")
        else:
            print("比实际数字大")
    i = i + 1
print(f"你猜了{i}次")
"""

#打印9*9乘法表
"""
i = 1
j = 1
while i <= 9:
    while j <= i:
        print(f"\t{i}*{j}={i*j}",end=' ')#,end=' '不换行
        j = j + 1
    j = 1
    i = i + 1
    print( )#换行
"""

#数一数有几个a
"""
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count = count + 1
print(f"有{count}个a。")
"""

#for嵌套 + range 打印9*9乘法表
"""
i = 1
j = 1
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"\t{i}*{j}={i*j}",end='')
    print()
"""

#循环中断 continue break 发工资
"""
import random # 随机数
money = 10000
i = 0
for i in range(1,21):
    num = random.randint(1, 10)
    if money > 0:
        if num < 5:
            print(f"员工{i}，绩效分{num}，小于5，不发工资，下一位。")
            continue
        else:
            print(f"向员工{i}，发放工资1000元，账户余额还剩余{money}元。")
            money = money - 1000
    else:
        print("工资发完了，下个月再来领取吧")
        break
"""