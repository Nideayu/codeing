'''
字典的常见操作
'''
# 修改元素
    # 字典的每个元素中的数据是可以修改的，只要通过key找到，就可以修改

info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
newId = input('请输入新的学号')
info['id'] = int(newId)
print('修改之后的id为%d:'%info['id'])


# 删除元素
    # 对字典进行删除操作，有一下几种：

    # del
    # clear()
info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

print('删除前,%s'%info['name'])

del info['name']

print('删除后,%s'%info['name'])