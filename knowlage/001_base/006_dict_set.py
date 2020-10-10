
''' dict '''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Lucy'] = 80
print(d)
# in  判断是否在dict中
print('Lucy' in d)
# 获取值
print(d.get('Lucy'))
# 删除元素
print(d.pop('Lucy'))
print(d)

'''set '''
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

# 交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)