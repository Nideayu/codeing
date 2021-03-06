'''
1.定义函数
    定义函数的格式如下：
        def 函数名():
            代码
'''
'''
2.调用函数
定义了函数之后，就相当于有了一个具有某些功能的代码，
想要让这些代码能够执行，需要调用它
    调用函数很简单的，
    通过 函数名() 即可完成调用

    函数的文档说明:
    可以用help()来调用函数
'''
# def age():
#     print('阿钰')
#     print('20')
# print(help(age()))


'''
3.函数的参数
    定义时小括号中的参数，用来接收参数用的，称为 “形参”
    调用时小括号中的参数，用来传递给函数用的，称为 “实参”

    缺省参数
    缺省参数调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    下例会打印默认的age，如果age没有被传入：
        def printinfo( name, age = 35 ):
            # 打印任何传入的字符串
            print "Name: ", name
            print "Age ", age
        # 调用printinfo函数
        printinfo(name="miki" )
        printinfo(age=9,name="miki" )

        输出
            Name:  miki
            Age  35
            Name:  miki
            Age  9

    不定长参数
        有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名。
        def functionname([formal_args,] *args, **kwargs):
            "函数_文档字符串"
            function_suite
            return [expression]


'''
'''
4.函数的返回值
    所谓“返回值”，就是程序中函数完成一件事情后，最后给调用者的结果

'''
'''
5.局部变量和全局变量
    局部变量
        就是在函数内部定义的变量
        不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响
        局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用
        print()函数打印遵循就近原则
    全局变量
        如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量
        在函数外边定义的变量叫做全局变量
        全局变量能够在所有的函数中进行访问
        如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
        如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
        在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
        对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
        对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。
'''

