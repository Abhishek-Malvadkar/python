#Find the Runner-Up Score! Problem 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])

or 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])

#My reference for this problem: 
#https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=19