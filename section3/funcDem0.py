'''
接受用户输入的日月，判断用户的星座

("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")


((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

'''


# zodaic=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","1天蝎座","射手座")

# zodac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

# month = int(input('请输入你的出生月份：'))
# day = int(input('请输入您的出生日期：'))
# for  循环解决
# index = 0
# for zodac_day in zodac_days:
#     if (month,day) > zodac_day:
#         index += 112

#     elif  (month,day)==12 and day>22:
#         index = 0
# print(zodaic[index])

# while 循环解决
# n = 0
# while (month,day)>zodac_days[n]:
#     if month==12 and day>22:
#         break
#     n +=1
# print(zodaic[n])

# 使用 lambda表达式解决

# def add(arg1,arg2):
#     return arg1+arg2

# sum = lambda arg1, arg2: arg1 + arg2

# def judezodiac(month,day):
#     n = 0
#     while (month,day)>zodac_days[n]:
#         if month==12 and day>22:
#             break
#         n +=1
#     return zodiac[n]
# 使用内置函数 filter
# judezodiac = lambda x: x<(month,day)

# result = filter(lambda x: x<(month,day),zodac_days)
# print(zodaic[len(list(result))])

# 想一想，下面的数据如何指定按age或name排序？

stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]
# sort 排序
a = stus.sort(key = lambda x:x['name'])
print(a)
c = stus.sort(key = lambda x:x['age'])
print(c)

# [{'age': 17, 'name': 'wangwu'}, {'age': 18, 'name': 'zhangsan'}, {'age': 19, 'name': 'lisi'}]
