print('作业1')
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
print("""******************
姓名：{0}
性别：{2}
年龄：{1}
******************""".format(name,age,sex))

print('#####################################################')


print('作业2')
str1 = "python hello aaa 123123aabb"
print(str1[:6])  #取值Python

str2 = str1.replace('python','lemon')   #替换Python为lemon
print(str2)

print('o a' in str1)   # o a
print('he' in str1)   # he
print('ab' in str1)   # ab

print(str1.find("aaa"))#找aaa起始位置




