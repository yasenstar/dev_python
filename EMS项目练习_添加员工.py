#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:36:15 2020
@author: yasen
"""

print("="*15, " 欢迎使用员工管理系统 ", "="*15)

    
# 创建一个列表，用来保存员工的信息，以字符串的方式保存
emp = []
emp = ['孙悟空\t18\t男\t花果山', '白骨精\t18\t女\t白骨山', '猪八戒\t28\t男\t高老庄']

# 创建一个死循环
while True:
    # 显示用户的选项
    print("请选择要做的操作：")
    # print(" "*8, "1、查询员工")
    # print(" "*8, "2、添加员工")
    # print(" "*8, "3、删除员工")
    # print(" "*8, "4、退出系统")
    print("\t1、查询员工")
    print("\t2、添加员工")
    print("\t3、删除员工")
    print("\t4、退出系统")
    user_select = input("请选择（1-4）： ")
    
    # print("你选择的是：", user_select)
    print("="*62)
    
    # 根据用户选择进行相应的操作
    if user_select == '1':
        # 查询员工
        # 打印表头
        print('\t序号\t姓名\t年龄\t性别\t住址')
        # 创建一个变量，来表示员工的序号
        n = 1
        # 显示员工信息
        for e in emp:
            print(f'\t{n}\t{e}')
            n += 1
    elif user_select == '2':
        # 添加员工
        # 获取要添加员工的信息：姓名、年龄、性别、住址
        emp_name = input("请输入要添加员工的姓名： ")
        emp_age = input("请输入要添加员工的年龄： ")
        emp_gender = input("请输入要添加员工的性别： ")
        emp_address = input("请输入要添加员工的住址： ")
        
        # 创建一个员工
        emp_new = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        
        # 显示一个提示信息
        print('员工：', emp_name, '将会被添加到系统中，是否确认该操作？[Y/N]：')
        user_confirm = input()
        
        # 判断
        if user_confirm == "y" or user_confirm == 'yes':
            # 确认
            # 将四个信息拼接为一个字符串，然后插入到列表中
            emp.append(emp_new)
            print('添加成功')
        else:
            print('添加已取消')

    elif user_select == '3':
        # 显示员工信息
        n = 1
        for e in emp:
            print(f'\t{n}\t{e}')
            n += 1
        
        # 获取用户希望删除的序号
        tobe_delete = int(input("请选择希望删除的员工序号： "))
        
        # 请用户确认删除
        print('员工：', emp[tobe_delete-1], '将会被删除，是否确认该操作？[Y/N]：')
        user_confirm = input()
        
        # 判断
        if user_confirm == "y" or user_confirm == 'yes':
            # 确认
            emp.pop(tobe_delete-1)
            print('删除成功')
        else:
            print('删除已取消')
        
    elif user_select == '4':
        # 退出
        input('欢迎使用！再见！')
        break
    else:
        print('您的输入有误，请重新选择！')

    print("-"*62)