# Uses python3
import sys


def optimal_weight(W, w):
    n = len(w)
    matrix = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            elif matrix[i-1][j-w[i-1]] + w[i-1] <= W:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-w[i-1]] + w[i-1])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[i][j]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
