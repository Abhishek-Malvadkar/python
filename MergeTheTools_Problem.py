def merge_the_tools(string, k):
    
    for i in range(0,len(string),k):  # k is step size of the factor
        a=[]
        for j in range(k): # this loop will look for the characters from the step value
            if string[i+j] not in a:
                a.append(string[i+j])
        b="".join(a)
        print(b)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)