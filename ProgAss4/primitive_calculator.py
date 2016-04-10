# Uses python3
import sys


def optimal_sequence(n):
    s1 = []
    while n >= 1:
        s1.append(n)
        if n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            if (n-1) % 9 == 0:
                n -= 1
            else:
                n //= 2
        else:
            n -= 1
    return reversed(s1)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
