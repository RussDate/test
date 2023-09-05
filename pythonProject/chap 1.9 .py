"""
#捕获异常
try:
    w = open("C:/Users/12645/Desktop/test.txt.back", "r", encoding="UTF-8")
except:
    print("出现异常，文件不存在")
    w = open("C:/Users/12645/Desktop/test.txt.back", "w", encoding="UTF-8")
"""

"""
#捕获指定/多个/所有/else异常
try:
    #print(name)
    1 / 0
except NameError as e:#指定
    print("发现NameError异常")
except (NameError,ZeroDivisionError) as e:#多个
    print("发现NameError,ZeroDivisionError异常")
except Exception as e:#所有
    print("发现异常")
else:#无异常执行
    print("好高兴，没有异常")
finally:#有无异常都执行
"""

#[from 模块名] import [模块|类|变量|函数| *（全部的意思）] [as 别名]