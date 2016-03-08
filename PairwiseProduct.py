# Uses python3
import random



def maxPairwiseBad(a,n):
    result = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if result < a[i]*a[j]:
                result = a[i]*a[j]
    return result

def maxPairwise(a, n):
    n1 = 0
    n2 = 0

    for i in a:
        if i > n1:
            n2 = n1
            n1 = i
        elif i > n2:
            n2 = i

    return n1 * n2


def test():
    while True:
        n = random.randrange(2, 1000)
        outer = n
        a = list(range(n))
        for i in range(n):
            a[i] = random.randrange(1, 100000)
        res1 = maxPairwise(a,n)
        res2 = maxPairwiseBad(a,n)
        print(n)
        print(a)
        if res1 != res2:
            print("Critical Failure: New -  %d; Old - %d" % (res1,res2))
            break



n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)

print(maxPairwise(a, n))