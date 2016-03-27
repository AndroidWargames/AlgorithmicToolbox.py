# Uses python3
import sys


def inversions(a):
    if len(a) <= 1:
        return [0,a]
    else:
        cut = len(a)//2
        a1 = a[:cut]
        a2 = a[cut:]
        return merge(inversions(a1),inversions(a2))


def merge(b, c):
    out = []
    count = b[0]+c[0]
    b, c = b[1], c[1]
    inv = len(b)
    runs = len(c) + inv
    for i in range(runs):
        if len(b) == 0:
            out.extend(c)
            break
        if len(c) == 0:
            out.extend(b)
            break
        if b[0] <= c[0]:
            out.append(b[0])
            del(b[0])
            inv -= 1
        else:
            out.append(c[0])
            del(c[0])
            count += inv
    return [count, out]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    x = inversions(a)[0]
