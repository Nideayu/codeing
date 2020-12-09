'''
if判断语句

if判断语句介绍

if语句是用来进行判断的，其使用格式如下：
    if 要判断的条件:
        条件成立时，要做的事情
'''

'''
练习
'''

age = input('请输入你的年龄：')
if age>=18:
    print('年龄达到18，可以去网吧')
else:
    print('未满18')


'''
if-else的使用格式
    if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)...
'''
'''
练习
'''

lon = input('请输入刀子的长度：')
if lon<10:
    print('允许上车')
else:
    print('不允许上车')

'''
elif的功能
elif的使用格式如下:


    if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3

当xxx1满足时，执行事情1，然后整个if结束
当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束
可以和else一起使用

if 性别为男性:
    输出男性的特征
    ...
elif 性别为女性:
    输出女性的特征
    ...
   else:
    第三种性别的特征
    说明:

当 “性别为男性” 满足时，执行 “输出男性的特征”的相关代码
当 “性别为男性” 不满足时，如果 “性别为女性”满足，则执行 “输出女性的特征”的相关代码
当 “性别为男性” 不满足，“性别为女性”也不满足，那么久默认执行else后面的代码，即 “第三种性别的特征”相关代码
elif必须和if一起使用，否则出错
'''
# 案列
score = 77

if score>=90 and score<=100:
    print('本次考试，等级为A')
elif score>=80 and score<90:
    print('本次考试，等级为B')
elif score>=70 and score<80:
    print('本次考试，等级为C')
elif score>=60 and score<70:
    print('本次考试，等级为D')
elif score>=0 and score<60:
    print('本次考试，等级为E')

'''
if 条件1:
    满足条件1 做的事情1
    满足条件1 做的事情2
    ...(省略)...
        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2
            ...(省略)...
'''
# 案列

chePiao = 1     # 用1代表有车票，0代表没有车票
daoLenght = 9     # 刀子的长度，单位为cm

if chePiao == 1:
    print("有车票，可以进站")
    if daoLenght < 10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有通过安检")
        print("刀子的长度超过规定，等待警察处理...")
else:
    print("没有车票，不能进站")
    print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")


# 案列

import random
player = input('请输入：剪刀（0） 石头（1） 布（2）')

player = int(player)

computer = random.randint(0,2)
# 用来进行测试
# print('player=%d,computer=%d',(player,computer)
if ((player==0))and (computer==2)or ((player==1))and (computer==0) or ((player==2))and ((computer==1)):
    print('恭喜你，你赢了')
elif player==computer:
    print('平局，要不要再来一局')
else:
    print('你输了')
    