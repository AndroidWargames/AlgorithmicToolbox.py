# Uses python3
import sys

def get_fibonaccihuge(n, m):
    a = [0,1]
    # standard output
    if n < 2:
        return a[n]
    # make a list of modulos
    for i in range(2,20000):
        a.append(a[i-2]+a[i-1])
    b = [x % m for x in a]
    print(b)
    # test for repeat cycles
    y = -1
    for i in range(2,19999):
        if b[i:i+2]==[0,1]:
            y = i
            break
    return b[n % y]

print(get_fibonaccihuge(100,100000))

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))

