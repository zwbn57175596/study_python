# 1. 栈的深度限制
import sys


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(sys.getrecursionlimit())
# print(fib(500))
# print(fib(10000))
# sys.getrecursionlimit() 返回的是python中对栈的深度限制，执行这段代码，很快就会报错
# 由于递归的次数太多了，所以超出了栈的深度限制


# 2. 尾递归
# 如果递归调用是子过程的最后一步，那么就是尾递归，上面的代码不是尾递归，因为计算fib(n)总是要先得到fib(n-1)和fib(n-2)，下面的代码是一个尾递归
def tail_fib(n, a, b):
    if n == 1:
        return a
    else:
        return tail_fib(n - 1, b, a + b)


print(fib(8))
print(tail_fib(9, 0, 1))


# 3. 利用尾递归突破栈深度限制
# 函数调用过程中，相关信息都保存在了栈中，对于尾递归同样如此，但是对于尾递归来说，每一次调用自身时，之前保存的那些信息都没有使用价值了，
# 道理就在于tail_fib执行结束之后，直接return了，根本不需要回到上一次调用它的函数中继续执行什么，所以先前放入栈中的信息都是没有价值的，
# 那么如果能利用那些旧的栈空间，就可以在不增加栈的深度的情况下放入新的函数调用信息。

class TailCallException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):
    def _wapper(*args, **kwargs):
        f = sys._getframe()
        # 当前帧的代码和当前帧的前一个帧的前一个帧的代码相同，此时，有三个帧
        if f.f_back and f.f_back.f_back and f.f_code == f.f_back.f_back.f_code:
            return TailCallException(args, kwargs) # 跑出异常
        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailCallException as e:
                    # 这里捕获到异常，同时也得到了函数执行时的参数， args 和  kwargs
                    # 抛出异常的函数退出了，那么它的帧也就被回收了
                    args = e.args
                    kwargs = e.kwargs
    return _wapper


@tail_call_optimized
def tail_fib(n, a, b):
    if n == 1:
        return a
    else:
        return tail_fib(n - 1, b, a + b)


print(tail_fib(100005, 0, 1))



