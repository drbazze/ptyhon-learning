#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    arr = []
    
    for _ in range(0,N):
        user_arrgs = input().strip().split(" ")

        if len(user_arrgs) < 1:
            continue

        command = user_arrgs[0]
        number = 0
        index = 0

        if len(user_arrgs) == 2:
            number = int(user_arrgs[1])
        elif len(user_arrgs) == 3:
            index = int(user_arrgs[1])
            number = int(user_arrgs[2])

        if command == "insert":
            arr.insert(index, number)
        elif command == "append":
            arr.append(number)
        elif command == "remove" and number in arr:
            arr.remove(number)
        elif command == "sort":
            arr.sort()
        elif command == "reverse":
            arr.reverse()
        elif command == "pop" and len(arr) > 0:
            arr.pop()
        elif command == "print":
            print(arr)