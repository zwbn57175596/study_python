
# 5. 常用的数据类型转换
num = 10
my_str = 'zs'
my_str1 = str(num)

my_str2 = '10'
num2 = int(my_str2)

print(my_str2)
print(num2)
print(type(num2))

# 6. 输入和输出
# 输出
print(1)
print('hello_world')

str1 = 'hello'
str2 = 'world'
# 输出多个变量的时候，中间要用 半角逗号 分隔
print(str1, str2)

# 修改分隔符（默认有一个空格）
print(str1, str2, sep='&')

# 修改换行符（默认有一个 \n）
print("hello", end='')
print("world")

# print??

# 输入
# str3 = input("请输入：")
# print(str3)
# python3 会把所有的input转为 字符串

# 输入多个值1
# str4 = input('请输入：').split(',') # 返回的是一个list
# print(str4)

# 7 格式化输出
name = 'zs'
age = 21

print('我叫%s, 年龄%d' % (name, age))

# format 格式化函数
print('我叫{}, 年龄{}' .format(name, age))
print('我叫{na}, 年龄{ag}' .format(na = name, ag = age))
print('我叫{0}, 年龄{1}' .format(age, name))
print('我叫{1}, 年龄{1}' .format(name, age))

# 8 运算符
# 算术运算符  略

# 成员运算符
# in 判断返回 True False
name_1 = 'abcd'
print('a' in name_1)
print('a' not in name_1)

# 逻辑运算符
# and or not

# 运算符优先级
# (and or not) < ( < > <= >=)
# or < and < not
print(True or True and False)
print(not True and True)

# if 判断 略

# 循环执行

# while
# num = 1
# while num <= 5:
#   num += 1
#   print(num)
# print('end')

# 注意： 循环的时候必须有结束条件

# for 循环
# for 变量名 in 条件:
#     执行语句

# 产生一个范围内的数据（特点， 包含起始， 不包含该结束)
# range(起始， 结束， 步长) 12345  135
print(list(range(1, 6, 2)))

# for in 产生 1-5
for value in range(1, 6):
    if value == 2:
        break
    print(value)

# break continue

