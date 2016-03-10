# Uses python3
import sys
import math

def optimal_summands(n):
    if n <= 2:
        return [n]
    # since this pattern optimizes using triangular numbers,
    # we can simply find the i-1th triangular number that
    # sums to n. Then we truncate it, and then the last number
    # will be the difference between the sum of the previous i-1
    # numbers our input, n.
    i = int(math.sqrt(2*n+1)-1)
    out = list(range(1,i))
    out.append(n-sum(out))
    return out
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
