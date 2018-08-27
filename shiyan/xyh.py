from functools import reduce
print(type(reduce(lambda x,y: x-y, [1, 2, 3, 4])))
print(list({1:4,2:4}))
print(type(iter([1,2,3])))
ff=iter([1,2,3])
print(list(map(lambda x:x**3,[x for x in ff if x>1])))
# def countdown(x):
#     while x >= 0:
#         yield x
#         x -= 1
#
# for i in countdown(10):
#     print(i)
iter_odd = (x for x in [1, 2, 3, 4, 5] if x % 2)

print(type(iter_odd))