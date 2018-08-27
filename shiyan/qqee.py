a=int(input())
b=[]
i=0
while i<a:
    b.append(int(input()))
    i=i+1
g=list(set(b))
g.sort()
for j in g:
    print(j)




#
# while 1:
#     try:
#         a=int(input())
#         b=[]
#         i=0
#         while i<a:
#             b.append(int(input()))
#             i=i+1
#         g=list(set(b))
#         g.sort()
#         for j in g:
#             print(j)
#     except:
#         break