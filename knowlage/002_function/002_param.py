
# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# 数组参数
def addEnd(L=[]):
    L.append('End')
    return L


print(addEnd([1,2,3]))
print(addEnd(['a', 'b', 'c']))
print(addEnd())
print(addEnd())


# 默认参数为None，避免上述问题（数组参数）
def addEnd2(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print(addEnd2())
print(addEnd2())


# 可变参数
def calc(numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum

print(calc([1,2,3,4,5,6,7]))


#  可变
def calc2(*numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum

print(calc2(1,2,3,4,5,6,7))

# list 传入可变参数  *list
l = [1,2,3,4,5,6,7]
print(calc2(*l))


# 关键字参数
def person(name, age, **kws):
    print('name:', name, 'age:', age, 'other:', kws)


person('Bob', 35, city='Beijing', job='Java')
person('Bob', 35)


# 命名关键字参数  指定名称
def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')
#person2('Jack', 24, job='Engineer')  # 报错
#person2('Jack', 24)  # 报错

# 命名关键字参数  简化调用
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person3('Jack', 24, job='Python')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1,2)  # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)  # a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

f2(1, 2, d=99, ext=None) # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print('f1(*args, **kw)===')
f1(*args, **kw)    # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)  # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}


def a(a,b,c):
    print(a, b, c)

ap = (1,2,3)
a(*ap)  # 1 2 3

''' 小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''