'''
    类的定义
'''

# class car:
#     pass


# class Car(object):
#     # 方法
#     def getCarInfo(self):
#         print ('这是一辆黄色的smart')
#     # 移动
#     def move(self):
#         print('car can move')
#     # 鸣笛
#     def toot(self):
#         print ('车在鸣笛。。滴滴')

# BMW =Car()
# BMW.move()
# BMW.toot()
# BMW.wheelNum = 4
# BMW.color = '褐色'
# print(BMW.color)


class Car:
    def __init__(self,color,wheelNum):
        self.color = color
        self.wheelNum = wheelNum
    def move(self):
        print('车在行驶~~~~~')
BMW = Car('red',4)
print(BMW.color)
print(BMW.wheelNum)
BMW.move()
Audio = Car('blue',40)
print(Audio.color)
print(Audio.wheelNum)
Audio.move()