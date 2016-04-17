# Uses python3

import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    inp = list(dataset)
    nums = []
    ops = []
    while len(inp) > 0:
        if len(inp) % 2 == 1:
            nums.append(int(inp[0]))
            del inp[0]
        else:
            ops.append(inp[0])
            del inp[0]
    n = len(nums)
    minmat = [[0 for x in range(n)] for x in range(n)]
    maxmat = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        minmat[i][i] = nums[i]
        maxmat[i][i] = nums[i]
    for s in range(1, n+1):
        for i in range(n-s):
            j = i + s
            mx = -10000000000
            mn = 10000000000
            for k in range(i, j):
                a = evalt(minmat[i][k], minmat[k+1][j], ops[k])
                b = evalt(maxmat[i][k], minmat[k+1][j], ops[k])
                c = evalt(minmat[i][k], maxmat[k+1][j], ops[k])
                d = evalt(maxmat[i][k], maxmat[k+1][j], ops[k])
                mn = min(mn, a, b, c, d)
                mx = max(mx, a, b, c, d)
            minmat[i][j] = mn
            maxmat[i][j] = mx
    return maxmat[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
