# 文件名批量修改工具

import os

print('''
1-当前文件夹
2-自定义文件夹
''')
c1 = int(input('请选择需要操作的文件夹：'))
if c1 == 1:
    dirname = './'
elif c1 ==2:
    dirname = input('请输入文件夹的路径：')
else:
    print('您的输入有误，请重新输入！')
filelist = os.listdir(dirname)
print(filelist)

print('''
请选择重命名操作：
1-在文件名的前端添加字符
2-在文件名的后端添加字符
3-在文件名中删除指定字符
''')

flag = int(input('请选择：'))  # 添加字符或删除字符

while True:
    if flag == 1:
        Adding = input('在文件名的前端添加以下字符：')
        yesno = input('执行修改：Y 或 N ？')
        if yesno == 'Y':
            for name in filelist:
                newname = Adding + '_' + name
                print(newname)
                os.rename(dirname+name, dirname+newname)
            break
    elif flag == 2:
        Adding = input('在文件名的后端添加以下字符：')
        yesno = input('执行修改：Y 或 N ？')
        if yesno == 'Y':
            for name in filelist:
                index = name.rfind('.')
                newname = name[:index] + '_' + Adding + name[index:]
                print(newname)
                os.rename(dirname+name, dirname+newname)
            break
    elif flag == 3:
        deleting = input('在文件名中需要删除的字符：')
        yesno = input('执行修改：Y 或 N ？')
        if yesno == 'Y':
            for name in filelist:
                index = name.find(deleting)
                if index == -1:
                    continue
                else:
                    lens = len(deleting)
                    newname = name[:index] + name[index + lens:]
                    print(newname)
                    os.rename(dirname+name, dirname+newname)
            break
    else:
        print('您的选择有误，请重新选择！')
