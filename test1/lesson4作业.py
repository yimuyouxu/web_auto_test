print("#1")
str1 = "1,summer,3.14"
list1 = list(str1)
print(list1)

print("*" * 20)

print("#2")
sum1 = 0
for i in range(1,6):
    sum1 += i
print("所有数字之和为{}".format(sum1))

print("*" * 20)

print("#3")
def funcition(a):
    if isinstance(a,list) == True:
        print("a是列表")
        if len(a)>5:
            print(True)
        else:
            print(False)
    elif isinstance(a,dict) == True:
        print("a是字典")
        if len(a)>5:
            print(True)
        else:
            print(False)
    elif isinstance(a, str) == True:
        print("a是字符串")
        if len(a)>5:
            print(True)
        else:
            print(False)
    else:
        print("a非列表、字典、字符串")
        if len(a)>5:
            print("False")
        else:
            print("False")
funcition({"a":1,"b":3,"c":5})

