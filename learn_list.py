# # 创建列表，通过[]创建列表
# my_list = [] # 创建一个空列表
# print(my_list, type(my_list))

# # 列表存储的数据，成为元素
# my_list = [10]
# print(my_list)

# 列表中多个元素用逗号隔开
# my_list = [10, 20, 30, 40, 50]
# print(my_list)
# print(my_list[1])
# 获取列表长度，得到列表的最大索引+1
# print(len(my_list))

# for i in range (0,5):
#     print(my_list[i])

# ============================
# 切片 语法：列表[起始:结束]
stus = ["孙悟空", "猪八戒", "沙和尚", "唐僧", "蜘蛛精", "白骨精"]
# print(stus[0:2])

# print(min(stus))

stus *= 2

print(stus)

print(stus.index("沙和尚",3))
print(stus.count("白骨精"))