# Uses python3
import sys

def get_fibonaccihuge(n, m):
    a = [0,1]
    # standard output
    if n < 2:
        return a[n]
    x = 0
    while True:
        x += 1
        a.append(sum(a[-2:]) % m)
        if a[-2:] == [0,1]:
            break
        if x > n:
            break
    return a[n % x]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))

