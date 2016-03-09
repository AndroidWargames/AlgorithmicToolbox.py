# Uses python3
import sys

def optimal_summands(n):
    if n <= 2:
        return [n]
    i = 0
    sum = 0
    while (n-sum)>(i+1)*2:
        i += 1
        sum += i
    out = list(range(1,i+1))
    out.append(n-sum)
    return out
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
