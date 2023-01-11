#String Formatting 

def print_formatted(number):
    for i in range (1,number+1):
        s = len(str(bin(number))[2:])
        print(str(i).rjust(s,' '),oct(i)[2:].rjust(s,' '),(hex(i)[2:].upper()).rjust(s,' '),bin(i)[2:].rjust(s,' '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#My reference for this problem: 
#https://www.codespeedy.com/python-string-rjust-and-ljust-methods/