# Uses python3
import sys

def get_change(n):
    a = n//10
    b = n % 10
    if b >=5:
        b -= 4
    return a+b

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
