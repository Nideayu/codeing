# python -m venv 虚拟环境名字
# 切换到cmd
# .\\env \\scripts\\activate\\
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