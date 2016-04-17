# Uses python3
import sys


def optimal_sequence(n):
    s = [10000000 for x in range(0,n+1)]
    i = 1
    s[i] = 0
    while i < n:
        i += 1
        a, b, c = 10000000, 10000000, 10000000
        if i//2 == i/2:
            a = s[i//2] + 1
        if i//3 == i/3:
            b = s[i//3] + 1
        c = s[i-1] + 1
        s[i] = min([a, b, c])
    o = [n]
    x = n
    while x > 1:
        a, b, c = 10000000, 10000000, 10000000
        if x//2 == x/2:
            a = s[x//2]
        if x//3 == x/3:
            b = s[x//3]
        c = s[x-1]
        if a <= b and a <= c:
            x //= 2
            o.append(x)
        elif b <= c and b <= a:
            x //= 3
            o.append(x)
        else:
            x -= 1
            o.append(x)
    return reversed(o)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
