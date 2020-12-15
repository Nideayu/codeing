def add():
    pass

def modify():
    pass

def update():
    pass




# 学生类
class Students:
    def __init__(self,score):
        self.score = score
        self.age = None
        self.id = None

    def get_score(self):
        return self.score
    def set_score(self):
        self.score = score



# 系统类
class System:
    def print_item(self):
        choice_num = int(input('''
        ''''''
        请选择
        
        ''''''
        '''))
        return choice_num

if __name__ == "__main__":
    student = Students()
    s = System()


    student.set_score(90)
    print(student1.score)
    print(s.print_item())