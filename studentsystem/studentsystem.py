# python -m venv 虚拟环境名字
# 切换到cmd
# .\\env \\scripts\\activate\\
def save(student):
    try:
        student_txt = open('filename','a')            # 以追加模式打开
    except Exception as e:
            student_txt = open('filename','w')        # 文件不存在，创建文件并打开
            for info in student:
                student_txt.write(str(info)+'\n')     # 按行存储，添加换行符
            student_txt.close()  
            
def insert():
    studentList =[]                                     # 保存学生信息的列表
    mark = True                                         # 是否继续添加
    while mark:
        id = input('请输入ID（如1001）：')
        if not id:                                      # ID为空，跳出循环
            break
        name = input('请输入姓名：')                    # name为空，跳出循环
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            c = int(input('请输入C语言成绩：'))
        except:
            print('输入无效，不是整数。。。重新输入')
            continue
        # 将输入的学生信息保存到字典
        stdent = {'id':id,'name':name,'english':english,'python':python,'c':c}
        studentList.append(stdent)                      # 将学生字典添加到列表中
        inputMak = input('是否继续添加？（y/n）')
        if inputMak =='y':                              # 继续添加
            mark =True
        elif inputMak == 'n':                           # 不能继续添加
            mark =False
        save(studentList)                               # 将学生信息保存到文件
        print('学生信息录入完毕')

def delete():
    mark = True                                                                        # 标记是否循环
    while mark:
        studentID = input('请输入你要删除学生的ID：')
        if studentID is not '':                                                        # 判断是否输入要删除的学生
            if os.path.exists('filename'):                                             # 判断文件是否存在
                with open('filename','r') as rfile:                                    # 打开文件
                    student_old = rfile.readlines()                                    # 读取全部内容
            else:
                student_old = []
                ifdel = False                                                          # 标记是否删除
                if student_old:                                                        # 如果存在学生信息
                    with open('fliename','w')as wfile:                                 # 以写的方式打开
                        d = {}                                                         # 定义空字典
                        for list in student_old:
                            d = dict(eval(list))                                       # 字符串转字典
                            if d[id] != studentID:
                                wfile.write(str(d)+'\n')                               # 将一条学生信息写入文件
                            else:
                                ifdel = True                                           # 标记已经删除
                        if ifdel:
                            print('ID为%s的学生信息已经被删除。。。' %studentID)
                        else:
                            print('没有找到%s的学生信息'% studentID)
                else:                                                                  # 不存在学生信息
                    print('无学生信息')
                    break                                                              # 退出循环
                show()                                                                 # 显示全部学生信息
                inputMark = input('是否继续删除？（n/y）：')
                if inputMark == 'y':
                    mark =True                                                         # 继续删除
                elif inputMark == 'n':
                    mark = False                                                       # 退出删除学生信息功能
                
def modift():
    show()  # 显示全部学生信息
    if os.path.exists('filename'):  # 判断文件是否存在
        with open('filename','r')as rfile:   # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
    else:
        return
    studentid = input('请输入要修改的学生ID：')
    with open('filename','w')as wfile:  # 以只写模式打开文件
        for student in student_old:
            d = dict(eval(student))  # 字符串转为字典
            if d['id'] == studentid:    # 是否要修改学生
                print('找到了这名学生，可以修改他的信息！')
                while True: # 输入要修改的信息
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = int(input('请输入英语成绩：'))
                        d['python'] = int(input('请输入Python成绩：'))
                        d['c'] = int(input('请输入C语言成绩：'))
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break   # 跳出循环
                student = str(d)    # 将字典转为字符串
                wfile.write(student+'\n')   # 将修改的信息写入到文件 
                print('修改成功！')
            else:
                wfile.write(student)    # 将未修改的信息写入到文件
    mark = input('是否继续修改其他学生信息？（y/n）:')
    if mark == 'y':
        modift()    # 重新执行修改操作


def menu():
    print('-'*30+'学生信息管理系统'+'-'*30)
    print('='*30+'功能菜单'+'='*30)
    print('''
    1.录入学生信息
    2.查找学生信息
    3.删除学生信息
    4.修改学生信息
    5.排序
    6.统计学生总人数
    7.显示所有学生信息
    0.退出系统
    
    ''')
    print('='*60)
    print('说明：可以通过数字或上下键头选择菜单')
    print('-'*60)
import os                                                   # 调用os模块
import re                                                   # 调用re模块
def main():
    ctrl = True                                             # 标记是否退出系统
    while (ctrl):                                            
        menu()                                              # 显示菜单
        option = input('请选择：')                           # 选择菜单项
        option_str = re.sub('\D',option)                    # 提取数字
        if option_str in ['1','2','3','4','5','6','7']:      
            option_int = int(option_str)
            if option_int == 0:                             # 退出系统
                print('您已经退出学生信息管理系统!')
                ctrl = False
            elif option_int == 1:                           # 录入学生成绩信息
                insert()
            elif option_int == 2:                           # 查找学生成绩信息
                search()
            elif option_int == 3:                           # 删除学生成绩信息
                delete()
            elif option_int == 4:                           # 修改学生成绩信息
                modify()
            elif option_int == 5:                           # 排序
                sort()
            elif option_int == 6:                           # 统计学生总数    
                total()
            elif option_int == 7:                           # 显示所有学生信息
                show()
if __name__ == "__main__":
    main()