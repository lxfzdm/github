#
# while 1:
#     y=int(input())
#     j=0
#     if y==0:
#         break
#     a=y//3
#     b=y%3
#     j=a
#     while 1:
#         y=a+b
#         a=y//3
#         b=y%3
#         j=j+a
#         if y==2:
#             j=j+1
#             print(j)
#             break
#         elif y==1 or y==0:
#             print(j)
#             break





# while 1:
#     try:
#         y=int(input())
#         #if y==0:
#         #    break
#         a=y//3
#         b=y%3
#         j=a
#         while 1:
#             y=a+b
#             a=y//3
#             b=y%3
#             j=j+a
#             if y==2:
#                 j=j+1
#                 print(j)
#                 break
#             elif y==1 or y==0:
#                 print(j)
#                 break
#     except:
#         break
# while 1:
#     try:
#         length=int(input())
#         b=[]
#         for i in range(length):
#             b.append(int(input()))
#         c=[]
#         for i in range(1,length):
#             c.append(length+1)
#         c.insert(0,0)
#         for i in range(length):
#             for j in range(i+1,length):
#                 if j<=i+b[i] and c[i]+1<c[j]:
#                     c[j]=c[i]+1
#         print(c[length-1])
#     except:
#         break
a={1:3,4:5,6:7}
print(a.items())
print(dict(a.items()))
