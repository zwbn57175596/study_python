import enum
from enum import unique

class ColorCode(enum.Enum):
    RED = 1
    BLUE = 2
    BLACK = 3

def print_color(color_code):
    if color_code == ColorCode.RED.value:
        print("红色")
    elif color_code == ColorCode.BLUE.value:
        print("蓝色")
    elif color_code == ColorCode.BLACK.value:
        print("黑色")

print_color(3)

# 枚举值一旦定义，不能修改，执行时会报错
# ColorCode.RED = 0

# 4.1 枚举值唯一
# 为了防止定义枚举值时出现重复的值， enum模块还提供了uniq装饰器
@unique
class ColorCode1(enum.Enum):
    RED = 1
#    BLUE = 1
    BLACK = 3


# 4.2 枚举值遍历
# 使用for循环可以对枚举值遍历
for color in ColorCode:
    print(color.name, color.value)

# 4.3 枚举值比较
# 枚举值之间不支持 < 和 > 操作，但是支持等值比较和is身份比较



