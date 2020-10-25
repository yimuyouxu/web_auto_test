# list1 = [20,"有序",3.14,"python",[1,2,3,4,5]]  #建一个列表
# # # print(type(list1))  #打印类型
# # # print(list1)  #打印列表
# # # print(list1[1])  #取单个值  有序
# # # print(list1[1:4:1])  #取多个值  取出来的是列表
# # # print(list1[4][3])
# # # print(list1[2:])
# list1 = ["有序",True,20,3.14,[1,2,3,4,5]]
# list1.append("python")
# list1.insert(3,"柠檬班") #在20后面增加元素
# list1.extend(["饼干","面包","披萨","烤鸭","豆腐脑汤","炒饭"])
# list1.pop(2)
# list1.remove(3.14)
# # list1.clear()
# list1[3] = "油条"
# list1[1] = "煎饼果子"
# list1.append("煎饼果子")
# print(list1)
# print(list1.count("煎饼果子"))
# print(len(list1))
# tuple1 = ('有序', '煎饼果子', '柠檬班', '油条', 'python', '饼干', '面包', '披萨', '烤鸭', '豆腐脑汤', '炒饭', '煎饼果子')
# print(tuple1[7:10:1])
# list1 = list(tuple1)
# print(list1)
# list1[-1] = "鸡蛋羹"
# print(list1)
# print(tuple(list1))
# dict1 = {"name":"Jackie","height":"175","weight":"140"}
# # print(dict1["height"])
# # print(dict1.get("weight"))
# # dict1["weight"] = 130
# # dict1["age"] = 18
# # dict1.pop("weight")
# # dict1.update({"city":"北京","hobby":"学习Python","gender":"male"})
# # print(dict1)
# list2 = [11,22,11,33,11,11]
# set1 = set(list2)  #转化为集合
# print(set1)
# print(list(set1))
# money = int(input("请输入你的余额："))
# if money >= 500:
#     print("买别墅！")
# elif money >= 200:
#     print("买一栋楼！")
# elif money >= 50:
#     print("买车！")
# else:
#     print("滚去工作赚钱！")
dict2 = dict(name="tricy",age=18)
print(dict2)