print("#1")
a = [1,2,"6","summer"]
print("i" in a)  #成员运算符判断
if "i" in a:
    print("i是成员")
else:
    print("i不是成员")
print("*" * 20)

print("#2")
dict_1 = {"class_id":45,'num':20}
if dict_1['num'] > 5:
    print("上课人数是{}".format(dict_1['num']))
else:
    print("上课人数不足5人")

print("*" * 20)

print("#3")
list3 = ["方方土","七木","荷花鱼","kingo","Amiee","焕蓝"]
dict_1 = ({"name":"方方土","gender":"female","age":18,"city":"北京"})
dict_2 = ({"name":"七木","gender":"female","age":19,"city":"上海"})
dict_3 = ({"name":"荷花鱼","gender":"female","age":20,"city":"广州"})
dict_4 = ({"name":"kingo","gender":"male","age":19,"city":"深圳"})
dict_5 = ({"name":"Amiee","gender":"female","age":22,"city":"长沙"})
dict_6 = ({"name":"焕蓝","gender":"male","age":19,"city":"北京"})
list_1 = [dict_1,dict_2,dict_3,dict_4,dict_5,dict_6]
# list_1.extend([dict_1,dict_2,dict_3,dict_4,dict_5,dict_6])
print(list_1)

list2 = ["female","female","female","male","female","male"]
list1 = [18,19,20,19,22,19]
list4 = ["北京","上海","广州","深圳","长沙","北京"]
list_2 = []
for i in range(6):
    dict1 = dict(name=list3[i],gender=list2[i],age=list1[i],city=list4[i])
    list_2.append(dict1)
print(list_2)
