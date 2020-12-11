'''
    读取name.text中的名字，存放在列表中
'''
f = open('./name.txt','r')
content =f.read().split('|')
print(content)
'''
    读取weapon.txt中的武器
'''
 
f1 = open('./weapon.txt','r+',encoding='utf-8')
# print(f1.readlines())
index = 0
for line in f1.readlines():
    data = line.strip()
    if index%2 ==0:
        print(data)
    index += 1
'''
    读取sanguo.txt
'''
f2 = open('./sanguo.txt','r+',encoding='GB18030')
print(f2.read())

f3 =open('./sanguo_utf8.txt','r+',encoding='utf-8')
print(f3.read())