
l = list(range(100))
print(l)

# dict 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for val in d.values():
    print(val)


# 字符串 迭代
for ch in 'ABC':
    print(ch)

# 只要对象可迭代，就可以用 for， 判断是否可迭代
from collections.abc import Iterable
print(isinstance('abceee', Iterable))   # True
print(isinstance([], Iterable))     # True
print(isinstance(123, Iterable))    # False

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


for i, value in enumerate([1, 2, 3]):
    print(i + value)


# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

L = [1,3,3,1]
print([1, *[v + L[i + 1] for i, v in enumerate(L) if (i < len(L) - 1)], 1])