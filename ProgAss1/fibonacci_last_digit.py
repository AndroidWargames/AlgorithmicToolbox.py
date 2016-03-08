# Uses python3
import sys


def get_fibonacci_last_digit(n):
    a = [0,1]
    if n < 2:
        return a[n]
    for i in range(n-1):
        a.append((a[0]+a[1])%10)
        del a[0]
    return a[1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

