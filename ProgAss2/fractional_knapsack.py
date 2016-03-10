# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    vbw = []
    #sort dat
    for i in range(len(weights)):
        vbw.append(values[i]/weights[i])
    outs = list(zip(vbw,weights,values))
    outs = sorted(outs, reverse=True)
    while capacity > 0 and len(outs) > 0:
        m = min(capacity,outs[0][1])
        capacity -= m
        value += m * outs[0][0]
        del outs[0]
    return round(value,4)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
