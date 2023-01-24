from itertools import combinations

N = int(input())
lst = list(input().split())
k = int(input())

tuples = list(combinations(lst,k))
count=0
for i in tuples:
    if 'a' in i:
        count = count+1
print(round(count/len(tuples),3))

# ref: https://docs.python.org/3/library/itertools.html