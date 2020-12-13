# 字符串格式化高级用法

# 1. %操作符
# 1.1 格式符
str_format = "I'm %s. I'm %d years old"
string = str_format % ('lilei', 14)
print(string)


# 2.1 format一般用法
log = "{id}-{type}-{msg}"
print(log.format(id = 1, type = 'debug', msg = '测试日志'))


# 2.2 与字典结合的用法
info = {
    'id': 1,
    'type': 'debug',
    'msg': u'测试连接'
}
log = "{0[id]}-{0[type]}-{0[msg]}".format(info)
print(log)


# 2.3 与tuple结合的用法
tp = (1, 'debug', u'测试连接1')
log = "{0[0]}-{0[1]}-{0[2]}".format(tp)
print(log)

log = "{info[0]}-{info[1]}-{info[2]}".format(info=tp)
print(log)


# 2.4 与对象结合的方法
class Info(object):
    def __init__(self, id, type, msg):
        self.id = id
        self.type = type
        self.msg = msg

info = Info(1, 'debug', '测试连接2')
log = "{info.id}-{info.type}-{info.msg}".format(info = info)
print(log)


# 2.5 不指定关键字参数
# 使用format方法时，如果为了方便，也可以不指定关键字参数，而是依据参数顺序格式化字符
log = "{}-{}-{}"
print(log.format(1, 'debug', '测试连接3'))


# 2.6 控制宽度
for i in range(1, 10):
    line = ""
    for j in range (1, i + 1):
        line += "{left} * {right} = {product} ".format(left = i, right = j, product = i * j)
    print(line)

# 注意看第三列，明显没有对齐，原因在于第2列的乘机出现了大于10的情况。为了能更美观的显示效果，我们需要控制格式化字符串是的宽度
# 只需要将带格式化的字符串稍稍做一下修改即可
for i in range(1, 10):
    line = ""
    for j in range (1, i + 1):
        line += "{left} * {right} = {product:2}\t".format(left = i, right = j, product = i * j)
    print(line)
# 我们制定product被格式化后占2个字符的宽度，这样，不论乘机是否大于10，都占2个字符的宽度


# 3.1 f-string用法
# f-string, 亦称为格式化字符串常量 ( formatted string literals )，是python3.6新引入的一种字符串格式化方法。
# f-string让字符串格式化更加简便，本质上f-string不是字符串常量，而是一个可以在运行时运算求值的表达式
color = 'red'
string = f'I like {color}'
print(string)
string = f'I like {color.upper()}'
print(string)
