from collections import namedtuple
n=int(input())
std=namedtuple('std',input().split())
sum_=0
for i in range(n):
    sum_+= int(std(*input().split()).MARKS)
print(sum_ /n )   

#MyReference: https://realpython.com/python-namedtuple/ 