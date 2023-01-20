from collections import Counter
n =  int(input())
li = list()
for _ in range(n):
    li.append(input())
ctr = Counter(li)
print(len(ctr))
print(*ctr.values())

# * is unpack operator, else it will be populated in the form of dictionary values
# counter is used to count the number of occurences of a particular value in the given number of lists