# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    vbw = []
    #sort dat
    for i in range(len(weigths)):
        vbw[i] = values[i]/weights[i]
    weights = [weights for (vbw,weights) in sorted(zip(vbw,weights))]
    values  = [values for (vbw,values) in sorted(zip(vbw,values))]
    while capacity > 0 and len(vbw) > 0:
        m = min(capacity,weights[0])
        capacity -= m
        value += m* values[0]
        del values[0]
        del weights[0]
        del vbw[0]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
