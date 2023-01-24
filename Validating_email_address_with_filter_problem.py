def fun(s):
    import re
    if(re.search(r"^[\w,-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$",s)):
        return True
    else:
        return False

#\w will cover only [a-z],[A-Z] and [0-9]
#+ means one occurance or more
 


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#ref: https://docs.python.org/3/library/re.html#:~:text=A%20regular%20expression%20(or%20RE,down%20to%20the%20same%20thing).