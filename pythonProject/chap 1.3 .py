
#if
"""
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快！")
"""

#if else
"""
print("欢迎来到黑马动物园")
height = int(input("请输入您的身高（cm）："))
if height >= 120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快。")
"""

#if elif else
"""
if int(input("请输入第一次猜想的数字：")) == 10:
    print("恭喜你，回答正确")
elif int(input("不对，请再猜一次：")) == 10:
    print("恭喜你，回答正确")
elif int(input("不对，再猜最后一次：")) == 10:
    print("恭喜你，回答正确")
else:
    print("sorry，全部猜错了，我想的是10")
"""

#嵌套猜数字if
"""
import random # 随机数
num = random.randint(1,10)
guess = int(input("请你开始猜数字："))
if guess == num:
    print("恭喜你回答正确！")
else:
    if guess < num:
        print("比实际数字小")
    else:
        print("比实际数字大")
    guess = int(input("请再猜一次："))

    if guess == num:
        print("恭喜你回答正确！")
    else:
        if guess < num:
            print("比实际数字小")
        else:
            print("比实际数字大")
        guess = int(input("请再猜一次,这是最后机会："))

        if guess == num:
            print("恭喜你回答正确！")
        else:
            print(f"抱歉，回答错误！答案为{num}")
"""
