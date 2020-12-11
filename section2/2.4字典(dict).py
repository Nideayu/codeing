'''
字典的常见操作
'''
# 修改元素
    # 字典的每个元素中的数据是可以修改的，只要通过key找到，就可以修改

# info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
# newId = input('请输入新的学号')
# info['id'] = int(newId)
# print('修改之后的id为%d:'%info['id'])


# 删除元素
    # 对字典进行删除操作，有一下几种：

    # del
    # clear()
# info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

# print('删除前,%s'%info['name'])

# del info['name']

# print('删除后,%s'%info['name'])


'''
无限次接受输入用户胡的点月日，判断用户的生肖和星座，并且统计出各个生肖和星座的次数
用什么类型的数据来接受统计出来的生肖和星座的次数

'''
chinese_zodiacs = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiacs=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

# chinses_zodiacs_dict ={}
# for chinses_zodiac in chinese_zodiacs:
#     chinses_zodiacs_dict[chinses_zodiac] = 0

# times = [0,0,0,0,0,0,0,0,0,0,0,0,]
# chinese_zodiacs = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# for  times,chinses_zodiac in zip(times,chinese_zodiacs):
#     chinses_zodiacs_dict[chinses_zodiac]=0


# 字典的推导式
# {key:value:for key in keys}
chinses_zodiacs_dict = {chinses_zodiac:0 for chinses_zodiac in chinese_zodiacs}
zodiac_dict = {zodiac:0 for zodiac in zodiacs} 

while True:
    year = int(input('请输入你的出生年份：'))
    month = int(input('请输入你的出生月份：'))
    day = int(input('请输入你的出生日期：'))
    num = 0
    for zodiac_day in zodiac_days:
        if (month,day)>zodiac_day:
            num += 1
        elif month==12 and day>22:
            num=0
    chinses_zodiacs_dict[chinese_zodiacs[year%12]]+=1

    zodiac_dict[zodiacs[num]] +=1

print(chinses_zodiacs_dict)
print(zodiac_dict)





