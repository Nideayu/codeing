'''
    id()
    __str__
'''

class Car:
    # 初始化方法
    def __init__(self,name,color='red',wheelNum=4):
        self.name = name
        self.color =color
        self.wheelNum = wheelNum

    def move(self):
        print('%颜色的汽车在运行~~~~'%self.color)
    def __str__(self):
        return '我是一辆%s车' % self.name
    def get_color(self):
        return
    def get_move(self):
        self.move()
    # 析构方法
    def __del__(self):
        print('我被删除了')
BMW = Car(name='baoma',color='blue',wheelNum=4)
print(BMW)

#定义一个home类
class Home:

    def __init__(self, area):
        self.area = area #房间剩余的可用面积
        #self.light = 'on' #灯默认是亮的
        self.containsItem = []

    def __str__(self):
        msg = "当前房间可用面积为:" + str(self.area)
        if len(self.containsItem) > 0:
            msg = msg + " 容纳的物品有: "
            for temp in self.containsItem:
                msg = msg + temp.getName() + ", "
            msg = msg.strip(", ")
        return msg

    #容纳物品
    def accommodateItem(self,item):
        #如果可用面积大于物品的占用面积
        needArea = item.getUsedArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea
            print("ok:已经存放到房间中")
        else:
            print("err:房间可用面积为:%d,但是当前要存放的物品需要的面积为%d"%(self.area, needArea))


#定义bed类
class Bed:

    def __init__(self,area,name = '床'):
        self.name = name
        self.area = area

    def __str__(self):
        msg = '床的面积为:' + str(self.area)
        return msg

    #获取床的占用面积
    def getUsedArea(self):
        return self.area

    def getName(self):
        return self.name


#创建一个新家对象
newHome = Home(100)#100平米
print(newHome)

#创建一个床对象
newBed = Bed(20)
print(newBed)

#把床安放到家里
newHome.accommodateItem(newBed)
print(newHome)

#创建一个床对象
newBed2 = Bed(30,'席梦思')
print(newBed2)

#把床安放到家里
newHome.accommodateItem(newBed2)
print(newHome)



#人类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + "剩余血量为:" + str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue -= shashangli

#弹夹类
class Danjia:
    def __init__(self, rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.rongnaList)) + "/" + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)

    def chuzidan(self):
        #判断当前弹夹中是否还有子弹
        if len(self.rongnaList) > 0:
            #获取最后压入到单间中的子弹
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None

#子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

#枪类
class Qiang:
    def __init__(self):
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪当前有弹夹"
        else:
            return "枪没有弹夹"

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia


    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("没有子弹了，放了空枪....")


#创建一个人对象
laowang = Ren("老王")

#创建一个弹夹
danjia = Danjia(20)
print(danjia)

#循环的方式创建一颗子弹，然后让老王把这颗子弹压入到弹夹中
i=0
while i<5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+=1
#测试一下，安装完子弹后，弹夹中的信息
print(danjia)

#创建一个枪对象
qiang = Qiang()
print(qiang)
#让老王，把弹夹连接到枪中
laowang.andanjia(qiang,danjia)
print(qiang)


#创建一个敌人
diren = Ren("敌人")
print(diren)

#让老王拿起枪
laowang.naqiang(qiang)

#老王开枪射敌人
laowang.kaiqiang(diren)
print(diren)
print(danjia)

laowang.kaiqiang(diren)
print(diren)
print(danjia)