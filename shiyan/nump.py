import numpy as np
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(type(b))
# print(b.dtype)
# print(b)
# print(b.shape)
# print(b[:,0:1].shape)
# print(b==1)
# b[b==1]=66
# print(b)
b=np.array(["1","2","3"])
print(type(b))
print(b.dtype)
b=b.astype(float)
print(b)
c=b.min(axis=0)
print(c)
d=np.array([[1,2,3],
            [4,5,6],
            [45,4,34]])
print(d)
print(d.sum(axis=0))
print(np.arange(15).reshape(3,-1))
print(d.ndim)
print(d.size)
print(np.zeros((3,5)))
print(np.ones((3,5)).astype(int))
print(np.arange(10,50,5))
a=range(2,10,2)
print(a)
print(list(a))
print(type(np.random.random((3,4))))
print(np.random.random((3,4)))

print(np.linspace(0,2*np.pi,2))

d=np.array([[1,2,3],
            [4,5,6],
            [45,4,34]])
e=np.array([[11,22,312],
            [42,5423,6123],
            [45213,421,34233]])
print(d-e)
print(d*e)
print(d**2)
print(d-1)
print(d<5)
print(d.dot(e))
print(np.dot(d,e))
print(np.exp(d))
print(np.sqrt(d))
d.reshape(-1,)
# d.shape=(-1,)

# d.reshape([9,1])等价于d.reshape((9,1))等价于d.reshape(9,1)等价于d.reshape(*(9,1))
print(d.reshape([9,1]))
print(d)
print(d.T)


A=np.floor(100*np.random.random((4,5)))
print(A.ravel())
print(A)


print(np.zeros((4,5)))

A=np.random.random((3,4))
B=np.random.random((3,4))
print(A,'\n'*2,B)
print("")
print(np.hstack((A,B)))
print(np.vstack((A,B)))

a=[11,2,3]
a.sort()
print(a)

b=np.hsplit(A,(2,3))
print(A)
for i in range(len(b)):
    print(b[i])

b=np.vsplit(A,(1,2))
print(A)
for i in b:
    print(i)
# for i in range(len(b)):
#     print(i)
# print(A)
# print(type(np.hstack((A,B))))
print(type(list(range(4))))
aaa=np.array([[3,4,5,6],[3,4,7,8]])
print(aaa)

print(aaa[0,1:3])

# 字符串的拆解和拼接
ab="sfdsfaafwrq"
c=ab.split("f")
print(c)
print("".join(["1","2","3"]))

# 复制，此种复制b就是a（内存相同）
a=np.arange(15)
b=a
a.shape=(3,5)
print(a,'\n'*2,b)
print(a is b)

#浅复制
a=np.arange(15)
b=a.view()
a.shape=(3,5)
print(a,'\n'*2,b)
a[1,0]=1
print(a,'\n'*2,b)

# 深度复制
a=np.arange(15)
b=a.copy()
a.shape=(3,5)
print(a,'\n'*2,b)
a[1,0]=1
print(a,'\n'*2,b)

aa=np.arange(15)
bb=aa
aa=np.arange(10)
print(aa,'\n',bb)
print(aa is bb)

l=[1,2,3,4]
p=l
l[1]=101
print(p,"\n",l)


a=np.arange(0,40,2)
b=np.tile(a,(3,1))
print(b)


a=np.random.random((7,5))
print(a)
c=a.argmax(axis=1)
print(c)


a=[1,2,3,231,232,23,1]
a.sort(reverse=True)
print(a)

def lx():
    print("sd")
    # return
a=lx()
print(a)

a="asfda"
c=a.index("f")
print(c)

a=np.random.random((3,4))
b=np.argsort(a,axis=0)
print(b)

a=np.random.random((3,4))
b=np.sort(a,axis=0)
c=np.argsort(a,axis=0)
print(a,'\n',b,'\n',c)

# 列表、字符串、元祖所使用的切片在矩阵中可以用
a=np.random.random((3,8))
print(a,'\n',a[1:2,-1::-1])






