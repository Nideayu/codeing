'''
使用for循环
为了更有效率的输出列表的每个数据，可以使用循环来完成
'''
# demo:
namesList = ['xiaoWang','xiaoZhang','xiaoHua']
for name in namesList:
    print(name)

'''

列表的相关操作

'''
# 添加：
    # append
    # 通过append可以向列表添加元素
    #定义变量A，默认有3个元素
A = ['xiaoWang','xiaoZhang','xiaoHua']
print("-----添加之前，列表A的数据-----")
for tempName in A:
    print(tempName)
#提示、并添加元素
temp = input('请输入要添加的学生姓名:')
A.append(temp)
print("-----添加之后，列表A的数据-----")
for tempName in A:
     print(tempName)


# 修改：
    # 通过索引来修改
    # 删除：del：根据下标进行删除
    # 定义变量A，默认有3个元素
A = ['xiaoWang','xiaoZhang','xiaoHua']
print("-----修改之前，列表A的数据-----")
for tempName in A:
        print(tempName)
    # 修改元素
A[1] = 'xiaoLu'
print("-----修改之后，列表A的数据-----")
for tempName in A:
        print(tempName)


# 删除
# del：根据下标进行删除
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
print('------删除之前------')
for tempName in movieName:
    print(tempName)

del movieName[2]

print('------删除之后------')
for tempName in movieName:
    print(tempName)

'''
列表嵌套
    类似while循环的嵌套，列表也是支持嵌套的

    一个列表中的元素又是一个列表，那么这就是列表的嵌套
'''
import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)    
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)