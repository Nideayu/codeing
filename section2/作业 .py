'''
# 1. 编程实现对一个元素全为数字的列表，求最大值、最小值
'''
# list = [1,2,3,4,5,6,7,8,9]
# # 最大值
# liasts = max(list)
# print(liasts)
# # 最小值
# lists = min(list)
# print(lists)

'''
2.编写程序，完成以下要求：
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
astr = 'hello world'
a = astr.count('h')
print(a)
'''

# 3. 编写程序，完成以下要求：
# 完成一个路径的组装
# 先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share

# while True:
#     aa =input('请输入你的路径,：')
#     b = input('输入q退出,如果输入q则不会在打印结果，输入除了q任意字符进行下一步：')
#     if b == 'q' :
#         break
#     while True:
#         bb = input('是否在进行插入路径，输入e则不会在询问')
#         if bb == 'e':
#             break
    
    
#         strs = aa+bb
#         a = '/'
#         c = a.join(strs)
#         print(c)


'''
4. 编写程序，完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''

# while True:
#     print('*'*30)
#     print('添加名片（1）')
#     print('删除名片（2）')
#     print('修改名片（3）')
#     print('查询名片（4）')
#     print('退出系统（0）')
#     print('*'*30)
#     qiut = input('输入你要执行的操作：')
#     if qiut == '0':
#         break