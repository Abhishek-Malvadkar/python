import numpy as nm

n,m = list(map(int,input().split()))
arr=[]
for i in range(0,n):
    arr.append(list(map(int,input().split())))
arr=nm.array(arr)

print(nm.mean(arr,axis=1))
print(nm.var(arr,axis=0))
print(round(nm.std(arr),11))

