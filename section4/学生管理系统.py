def add():
    num =input('请输入学号')
    name = input('请输入姓名')
    age = input('请输入年龄')
    performance = input('请输入成绩')
    f = open('/message.txt','a',encoding='utf-8')
    a = 'num:%s,name:%s,age:%s,performance:%s'%(num,name,age,performance)
    f.write(a)
    f.close()
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
        if num == '0':
            print('成功退出')
            break
        elif num == '1':
            print('=' * 30)
            add()
            print('插入成功')
            print('=' * 30)
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

if __name__ == '__main__':
    main()
