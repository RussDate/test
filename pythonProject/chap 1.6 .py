#数据容器
#列表list
"""
name_list = ['itheima','python']
a_list = ["itheima", 666 ,True]
my_list = [[1,2,3],[4,5,6]]#支持列表嵌套
print(name_list, a_list, my_list)

#下标索引
print(name_list[0])#从前往后索引
print(name_list[-2])#从后往前索引
print(my_list[0][1])#嵌套列表的索引

#列表操作
#查找元素下表索引
name_list.index("itheima")
print(name_list.index("itheima"))#列表.index（元素）

#修改特定索引的元素值
name_list[0] = "修改"#列表[下标] = 值
print(name_list)

#在指定下表位置插入元素
name_list.insert(1,"插入")#列表.insert（下标，元素）
print(name_list)

#追加元素（单个）
name_list.append("追加")#列表.append（元素）
print(name_list)

#追加元素（多个）
name_list.extend(a_list)#列表.extend（列表）
print(name_list)

#删除元素1
name_list = ['itheima','python']
del name_list[1]#del 列表[下标]
print(name_list)

#删除元素2
name_list = ['itheima','python']
element = name_list.pop(1)#列表.pop（下标）
print(f"通过pop方法取出的元素是{element},取出后的列表为{name_list}")

#删除元素3
name_list = ['itheima','itheima','python','python']
name_list.remove('itheima')#列表.remove（元素），删除列表中第一个‘匹配元素’
print(name_list)

#清空列表
name_list.clear()#列表.clear（）
print(name_list)

#统计特定元素数量
name_list = ['itheima','itheima','python','python']
count = name_list.count('itheima')#列表.count（元素）
print(f"name_list中itheima的数量为{count}个")

#统计列表中的元素个数
len = len(name_list)#list（列表）
print(f"name_list中的元素个数为{len}个")
"""
"""
#实操
mylist = [21, 25, 21, 23, 22, 20]
mylist.append(31)
print(f"追加数字31后，列表为{mylist}")
addlist = [29, 33, 30]
mylist.extend(addlist)
print(f"追加一个列表【29，33，30】后，列表为{mylist}")
element_1 = mylist.pop(0)
element_2 = mylist.pop(-1)
print(f"取出的第一个元素是{element_1},最后一个元素是{element_2}")
mylist.index(31)
print(f"元素31在列表中的位置是{mylist.index(31)}")
"""
"""
#列表遍历
#while方法
def list_while_func():
    mylist = [21, 25, 21, 23, 22, 20]
    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f"列表的元素：{element}")
        index = index + 1

def list_for_func():
    mylist = [21, 25, 21, 23, 22, 20]
    for element in mylist:
        print(f"列表的元素：{element}")

list_while_func()
print("-----------------------")
list_for_func()
"""
"""
#案例
def list_while_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newlist = []
    index = 0
    while index < len(mylist):
        element = mylist[index]
        if element % 2 == 0:
            print(f"{element}是偶数")
            newlist.append(element)
        index += 1
    print(f"通过while循环，从列表：{mylist}中取出偶数，组成新列表：{newlist}")

def list_for_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newlist = []
    for element in mylist:
        if element % 2 == 0:
            print(f"{element}是偶数")
            newlist.append(element)
    print(f"通过for循环，从列表：{mylist}中取出偶数，组成新列表：{newlist}")

list_while_func()
print("-----------------------")
list_for_func()
"""

"""
#字符串容器
my_str = "itheima and itcast"
#下表索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"{value} and {value2}")
#字符串不能修改

#index方法
value = my_str.index("and")#索引起始值
print(f"{value}")

#字符串的替换
new_my_str = my_str.replace("it", "程序")
print(f"{new_my_str}")#字符串.replace（字符串1，字符串2）2代替1

#字串的分割
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"{my_str_list}")

#字符串的去除
my_str = " itheima and itcast "
new_my_str = my_str.strip(" ")
print(f"{new_my_str}")#不含参数，去收尾空格

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"{new_my_str}")#含参数，会单独去除参数中的每一个字符

#统计字符串中某字符串中出现的次数 字符串.count（字符串）
#统计字符串的长度len（）
"""

#案例
my_str = "itheima itcast boxuegu"
count = my_str.count("it")
print(f"{my_str}中it出现的次数为{count}次。")
new_my_str = my_str.replace(" "," |")
print(f"{my_str},被替换空格后，结果：{new_my_str}")
new_str = new_my_str.split("|")
print(f"{new_my_str},按照|分割后，结果：{new_str}")