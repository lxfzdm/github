# # n,m=map(int, input().split())
# # print(n,m)
# # print(type(map(int, input().split())))
# # a=list("asfg afd  sadg")
# # print(a)
# a=[1,2,3]
# b=[4,5]
# a.append(b)
# print(a)
# (n,m)=map(int, input().split())



# num_gz,num_person=list(map(int,input().split()))
# i=0
# a=[]
# while i<num_gz:
#     a.append(list(map(int,input().split())))
#     i=i+1
# cable_person=list(map(int,input().split()))
# for ii in cable_person:
#     zui=0
#     for jj in a:
#         if jj[0]<=ii and jj[1]>=zui:
#             zui=jj[1]
#     print(zui)
#
#
#
num_gz,num_person=list(map(int,input().split()))
i=0
a=[]
while i<num_gz:
    h=input().split()
    if len(h)==2:
        a.append(list(map(int,h)))
        i=i+1
while 1:
    h=input().split()
    if len(h)==num_person:
        cable_person=list(map(int,h))
        break
# for ii in cable_person:
#     zui=0
#     for jj in a:
#         if jj[0]<=ii and jj[1]>=zui:
#             zui=jj[1]
#     print(zui)
from collections import defaultdict
dp = defaultdict(int, a)
ma=0
d=sorted(list(dp.keys())+cable_person)
for i in d:
    ma = max(dp[i], ma)
    dp[i]=ma
for i in cable_person:
    print(dp[i])








# N, M = list(map(int,input().split()))
# D = [0] * (N+M)
# P = [0] * (N+M)
# for i in range(N):
#     D[i],P[i] = list(map(int,input().split()))
# A = list(map(int,input().split()))
# D[N:] = A
# DP = [[d,p] for d,p in zip(D,P)]
# DP = sorted(DP)
# for i in range(1,N+M):
#     DP[i][1] = max(DP[i][1], DP[i-1][1])
# DP = dict(DP)
# for x in A:
#     print(DP[x])





a,b=list(map(int,input().split()))
#c=""
#d=""
#for i in range(a):
#    c=c+str(i+1)
#for d in range(b):
#    d=d+str(i+1)
q=0
k=0
while 1:
    if k>=a and k<=b:
        j=0
        for i in range(k+1):
            j=j+i
        if j%3==0:
            q=q+1
    k=k+1
    if k>b:
        break
print(q)