'''
例子：
    age = 18
    name = "xiaohua"
    print("我的姓名是%s,年龄是%d"%(name,age))

    %c	字符
    %s	通过str() 字符串转换来格式化
    %i	有符号十进制整数
    %d	有符号十进制整数
    %u	无符号十进制整数
    %o	八进制整数
    %x	十六进制整数（小写字母）
    %X	十六进制整数（大写字母）
    %e	索引符号（小写'e'）
    %E	索引符号（大写“E”）
    %f	浮点实数
    %g	％f和％e 的简写
    %G	％f和％E的简写

'''

'''
\n代表换行

'''

'''
练习：
'''

name= input('请输入名字')
QQ = input('请输入QQ')
iphone = input('请输手机号')
gosi = input('请输入公司地址')


print('='*30)
print('姓名：%s' %name)
print('QQ：%s' %QQ)
print('手机号：%s' %iphone)
print('公司地址：%s' %gosi)

print('='*30)