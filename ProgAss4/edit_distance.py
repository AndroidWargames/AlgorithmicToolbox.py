# Uses python3
def edit_distance(s, t):
    a = list(s)
    b = list(t)
    n = len(a)
    m = len(b)
    matrix = [[0 for x in range(m+1)] for x in range(n+1)]
    for i in range(0, m + 1):
        matrix[0][i] = i
    for i in range(0, n + 1):
        matrix[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                matrix[i][j] = min([matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]])
            else:
                matrix[i][j] = min([matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1])
    return matrix[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
