'''
1. 编程实现 9*9乘法表
提示：使用循环嵌套
'''

# def ase():
#     for i in range(1,10):
#         for c in range(1,10):
#             print('%d*%d=%-2d' % (i,c,i*c),end='')
#         print('\n')

# print(ase())
'''
2.用函数实现求100-200里面所有的素数
提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数

'''
'''
2. 编写“学生管理系统”，要求如下：
必须使用自定义函数，完成对程序的模块化
学生信息至少包含：姓名、年龄、学号，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询、退出

'''

def main():
    while True:
        print('学生管理系统')
        print('*'*30)
        print('添加信息(1)')
        print('修改信息(2)')
        print('查询信息(3)')
        print('退出信息(0)')
        print('*'*30)
        num = input('请输入你要进行的操作：')
        if num =='0':
            print('成功退出')
            break
        elif num == '1':
            def add()
        elif num == '2':
            print('='*30)
            print('修改信息')
            print('='*30)
        elif num == '3':
            print('='*30)
            print('查询信息')
            print('='*30)
        else:
            print('='*30)
            print('你的输入有误，请重新输入')
            print('='*30)

main()

def add():
    num =input('请输入学号')
    name = input('请输入姓名')
    age = input('请输入年龄')
    performance = input('请输入成绩')
    f = open('/message.txt','w+',encoding='utf-8')
    f.close()