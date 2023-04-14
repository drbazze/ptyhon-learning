"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())

    n = 5
    arr = set(map(int, "2 3 6 6 5".split()))

    print(sorted(arr)[-2])