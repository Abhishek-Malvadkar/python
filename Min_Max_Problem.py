import numpy

N,M = map(int,input().split())
li = []
for i in range(N):
    a=list(map(int,input().split()))
    li.append(a)
arr=numpy.array(li)

print(numpy.max(numpy.min(arr,axis=1)))