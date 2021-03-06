# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while right - left >= 0:
        m = (right + left) // 2
        if m >= len(a):
            break
        if x == a[m]:
            return m
        if x > a[m]:
            left = m+1
        else:
            right = m-1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
