'''import keyword
print(keyword.kwlist)
'''
# print("中文：我爱你")
# print("日文：あいしてる")
# print("英文：i love you")
# list_1 = [1,  2,3,4,5]
#
# list_2 = list_1[2:]
# print (list_2)
# print (5 /3)
sum_1 = 0
for i in range(101):
    sum_1 += i
print(sum_1)

num_1 = int(input("请输入一个数值："))
if num_1%2 == 0:    #判断是否是偶数，除2余数为0
    print("True,{}是偶数".format(num_1))
else:
    print("False,{}不是偶数".format(num_1))

list_1 = []
def function_1(num_1):
    for i in range(num_1):
        if i%2 == 0:
            list_1.append(i)
    print(list_1)
    sum_1 = 0
    for a in list_1:
        sum_1 += a
    print(sum_1)
function_1(101)
input("姓名：")
input("性别：")
input("年龄：")
dict_1 = {}
dict_1["姓名"] = input("请输入姓名：")
dict_1["性别"] = input("请输入性别：")
dict_1["年龄"] = input("请输入年龄：")
print(dict_1)
print('''我的名字{},今年{}岁,性别{},喜欢敲代码'''.format(dict_1["姓名"],dict_1["年龄"],dict_1["性别"]))
dict_1["身高"] = input("请输入身高：")
dict_1["联系方式"] = input("请输入联系方式：")
print(dict_1)
dict_1.pop("联系方式")
print(dict_1)