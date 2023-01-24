from collections import deque
T = int(input())
for i in  range(0,T):
    n = int(input())
    stack = []
    d = deque(map(int,input().split()))
 # evrytime one will get removed so use a loop to check for n times    
    for i in range(0,n):
        if(d[0]>=d[-1]):
            stack.append(d.popleft())
        elif(d[-1]>d[0]):
            stack.append(d.pop())
    #print(stack)
    #print(sorted(stack,reverse=True))
    # only if stack = sorted values then it can be piled up because 1st cube should be larger than 2nd cube
    if (stack==sorted(stack,reverse=True)):
        print('Yes')
    else:
        print('No')
		
		
Ref: https://docs.python.org/3/library/collections.html#collections.deque