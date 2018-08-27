# while 1:
#     try:
#         i=0
#         a,b=list(map(int,input().split()))
#         c=list(map(int,input().split()))
#         while i<b:
#             aa,bb,cc=input().split()
#             if aa=="Q":
#                 print(max(c[min({int(bb),int(cc)})-1:max({int(bb),int(cc)})]))
#             elif aa=="U":
#                 c[int(bb)-1]=int(cc)
#             i=i+1
#     except:
#          break


# a=list(input())
# b=set(a)
# c=list(b)
# d=[]
# for i in c:
#     d.append(a.index(i))
# d.sort()
# t=0
# bbb=[]
# for j in d:
#     bbb.append(a[j])
#     t=t+1
# print("".join(bbb))

# while 1:
#     try:
#         b = []
#         while 1:
#             a = input().split()
#             # print(a)
#             if not a:
#                 break
#             b.extend(a)
#             # print(b)
#
#     except:
#         print(len(list(set(b))))
#         break
# ii=0



# def zdf():
#     while 1:
#         a = input()
#         if not a:
#             break
#         if len(a) < 8:
#             print(a + "0" * ((8 - len(a))))
#         else:
#             b = len(a) // 8
#             c = len(a) % 8
#             for i in range(b):
#                 print(a[i * 8:((i + 1) * 8)])
#             if c != 0:
#                 print(a[len(a) - c:] + "0" * (8 - c))


# import sys
# a=[]
# for line in sys.stdin:
#     if line.strip() == '':
#         break
#     a.extend(line.split())
# print(len(set(a)))


from collections import defaultdict
# a,dd=int(input()),defaultdict(int)
# print(a,dd)
# # print(dd["s"])
# for i in range(a):
#     key,val=map(int,input().split())
#     dd[key]+=val
#     print(dd)
# for i in sorted(dd.keys()):
#     print(str(i)+" "+str(dd[i]))








# s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
# d = defaultdict(set)
# for k, v in s:
#   d[k].add(v)
#
# print(d)

# list = [1,2,2,3,4,2,3,3]
# d = dict()
# for element in list:
#     if element in d:
#         d[element]+=1
#     else:
#         d[element] = 1
#
# print(d.items())
a=[(3,4),(56,354)]

for i,j in a:
    print(i,j)