'''
单引号或者双引号的数据，就为字符串
print()字符串的输出
input()字符串的输入
'''

'''
切片：
    切片的语法：[起始:结束:步长]
    取前不去后 [0:2](0,1)
    
面试题给一个字符串aStr，请反转
从后往前取:  [-1:0]

'''

# replace:替换 把mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# aStr = 'asdasdasdasdasd'
# a = aStr.replace('a','cc')
# print(a)

# count:统计次数 返回str在start和end之间 在 mystr里面出现的次数
# aStr = 'asdasdasdasdasd'
# a = aStr.count('a')
# print(a)

# join：用于将序列中的元素以指定的字符连接生成一个新的字符串
# c = '-'
# aStr = ['a','b','c']
# a = c.join(aStr)
# print(a)
# 返回值a-b-c


#split:分割,返回值是列表
# aStr = 'asdasdasdasdasd'
# a = aStr.split('d')
# print(a)