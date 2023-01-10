#Finding the percentage Problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_marks = sum(student_marks[query_name]) / len(student_marks[name])
    print("{:.2f}".format(avg_marks))

#My reference for this problem: 
#https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3
#https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=19