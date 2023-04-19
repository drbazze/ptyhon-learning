#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    chars = []

    for char in s:
        if char.isupper():
            chars.append(char.lower())
        else:
            chars.append(char.upper())

    return "".join(chars)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)