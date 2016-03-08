# Uses python3
def calc_fib(n):
    a = [0,1]
    if n < 2:
        return a[n]
    for i in range(n-1):
        a.append(a[0]+a[1])
        del a[0]
    return a[1]

n = int(input())
print(calc_fib(n))


