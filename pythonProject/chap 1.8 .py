#打开文件,读取文件r
"""
open()#打开文件
read(num)#读取固定字节
readlines()#读取全部
readline()#读取固定行
for line in #循环读取每一行
close()#关闭文件
with open() as f #通过with open打开，可以自动关闭
"""
"""
f = open("C:/Users/12645/Desktop/test.txt","r",encoding = "UTF-8")
content = f.read()
count = content.count("王明旭")
print(f"{content}")
print(f"文件中一共出现了{count}次王明旭")
f.close()
"""
#写入 覆盖 w
"""
f = open("C:/Users/12645/Desktop/test.txt","w",encoding = "UTF-8")#"w"模式：写入文件不存在，会自动新建；文件存在写入会清空原文件内容
f.write("吴童")
f.flush()
f.close()
"""
#写入 a
"""
f = open("C:/Users/12645/Desktop/test.txt","a",encoding = "UTF-8")#"a"模式：写入文件不存在，会自动新建；文件存在写入到原内容最后
f.write(" 陈健鹏")
f.flush()
f.close()
"""

#
"""
r = open("C:/Users/12645/Desktop/test.txt","r",encoding = "UTF-8")
w = open("C:/Users/12645/Desktop/test.txt.back","w",encoding = "UTF-8")
for line in r:
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    w.write(line)
    w.write("\n")
w.flush()
r.close()
w.close()
"""
