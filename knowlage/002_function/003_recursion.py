# 递归

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(2))
print(fact(3))
print(fact(10))
print(fact(100))


# 尾递归
print('=================')
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact1(100))
print(fact1(900))

''' 调用过程
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''
