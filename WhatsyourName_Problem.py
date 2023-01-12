def print_full_name(first, last):
    # Write your code here
    a=print('Hello' + ' ' + first_name + ' ' + last_name+ '!'+ 
    ' '+ 'You just delved into python.')
    return a
# alternate: print('Hello {1} {0}! You just delved into python.'.format(b,a))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)