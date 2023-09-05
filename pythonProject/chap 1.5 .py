#函数
"""
def welcome():
    print("欢迎来到黑马程序员。")
    print("请出示您的健康码以及72小时核算证明。")

welcome()
"""

#加法
"""
def add(x,y):
    print(f"{x}+{y}={x+y}")

add(1,2)
"""
#体温
"""
def temp(temp):
    if temp <= 37.5:
        print(f"体温测量中，您的体温是：{temp}，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{temp}，需要隔离！")

print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
temp(37.3)
temp(39.3)
"""

#返回值
"""
def add(x,y):
    return x + y

a = add(1,2)
print(a)
"""

#ATM
"""
def main_table():
    print("--------------------------主菜单--------------------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    choose = int(input("请输入您的选择："))
    if choose == 1:
        check()
    elif choose == 2:
        deposit()
    elif choose == 3:
        withdrawal()
    else:
        print("退出成功！")
def check():
    print("--------------------------查询余额--------------------------")
    global money
    global name
    print(f"{name}，您好，您的余额剩余：{money}元")
    main_table()

def deposit():
    print("--------------------------存款--------------------------")
    global money
    global name
    cun = int(input("您要存款（元）："))
    money = money + cun
    print(f"{name}，您好，您存款{cun}元成功。")
    print(f"{name}，您好，您的余额剩余：{money}元。")
    main_table()

def withdrawal():
    print("--------------------------存款--------------------------")
    global money
    global name
    qu = int(input("您要取款（元）："))
    money = money - qu
    print(f"{name}，您好，您存款{qu}元成功。")
    print(f"{name}，您好，您的余额剩余：{money}元。")
    main_table()

name = input("请输入您的姓名：")
money = 5000000
main_table() 
"""
