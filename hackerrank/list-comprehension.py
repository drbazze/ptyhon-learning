"""
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    
    print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c) != n])