# Uses python3
import sys

def get_majority_element(a):
    rem = -1
    final = a
    lim = len(final)/2
    while True:
        b = []
        if len(a) % 2 == 1:
            rem = a[-1]
        size = len(a)//2
        if size == 0:
            break
        for i in range(size):
            if a[i] == a[i+size]:
                b.append(a[i])
        a = b
    if rem == -1:
        return 0
    j = 0
    for i in final:
        if i == rem:
            j += 1
    if j > lim:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))
