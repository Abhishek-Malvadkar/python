n,m = map(int,input().split())
arr = list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

print(sum((i in A) - (i in B) for i in arr))

# If array is present in set A then add 1, and if array is present in set B then substract 1 