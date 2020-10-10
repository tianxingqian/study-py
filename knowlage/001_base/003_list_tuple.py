'''list'''
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))


l = [1,2,3,4,5,6]
print(*l)


'''tuple'''
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 一个元素
t = (1,)
print(t)
# 复合
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


