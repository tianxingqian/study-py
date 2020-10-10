
# 列表生成式

#   列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#   举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#   方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

#   但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#   for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]
#   还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])    # 结果 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#   运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])     # ['001_slice.py', '002_Iteration.py', '003_list_Comprehensions.py', '__init__.py']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, v)

#   因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


# if else
print([x for x in range(1, 11) if x % 2 == 0])
# 但是，我们不能在最后的if加上else：
#print([x for x in range(1, 11) if x % 2 == 0 else 0])   # SyntaxError: invalid syntax
# if写在for前面必须加else，否则报错：
# print([x if x % 2 == 0 for x in range(1, 11)])  #SyntaxError: invalid syntax
print([x if x % 2 == 0 else -x for x in range(1, 11)])
# 总结，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。