# list1 = ["火锅","烤肉","咖喱","叉烧","烤鸭","石斑鱼","龙虾","鹅肝","鱼子酱","和牛","大阪烧","寿喜锅"]
# for name in list1:
#     print(name)
# count = 0
# list1 = ["火锅","烤肉","咖喱","叉烧","烤鸭","石斑鱼","龙虾","鹅肝","鱼子酱","和牛","大阪烧","寿喜锅"]
# for name in list1:
#     if name == "咖喱":
#         # break  #跳出循环
#         continue
#     print(name)
#     count += 1
# print(count)
# print(len(list1))
# for i in range(1,5,1):
# #     print(i)
def good_job(salary,*args,bonus,subsidy=500): #salary,bonus,subsidy是函数的参数，没有具体的值，形式上的参数---形参（用变量来替代）
    sum1 = salary + bonus + subsidy  #sum1是函数实现的功能
    print("salary的值{}".format(salary))
    print("bonus的值{}".format(bonus))
    print("subsidy的值{}".format(subsidy))
    print("args的值{}".format(args))
    print("这个工作的工资总和是{}".format(sum1))
good_job(8000,2000,800,50,100,200)