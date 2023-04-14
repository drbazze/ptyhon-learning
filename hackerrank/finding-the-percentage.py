# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # student_marks = {
    #     "Krishna": [67,68,69],
    #     "Arjun": [70,98,63],
    #     "Malika": [52,56,1]
    # }

    print(f"{sum(student_marks[query_name]) / 3:.2f}")