#https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    #No duplications
    stamps = set()

    for _ in range(n):
        stamps.add(input())
    print(len(stamps))