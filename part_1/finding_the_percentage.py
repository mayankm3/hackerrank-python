# https://www.hackerrank.com/challenges/finding-the-percentage?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    totalSum = sum(student_marks[query_name])
    avg=totalSum/3
    print(f"{avg:.2f}")

