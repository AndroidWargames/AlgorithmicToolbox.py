# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts = merge_sort(starts)
    ends = merge_sort(ends)
    for i in range(len(points)):
        p = points[i]
        s = hi_seek(starts, p)
        e = lo_seek(ends, p)
        cnt[i] = len(starts) - s - e
    return cnt


def hi_seek(a,x):
    r = len(a) - 1
    l = 0
    while True:
        m = (r + l) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
        if r == l:
            if a[r] < x:
                r += 1
            if len(a) != r:
                if a[r] == x:
                    r += 1
            break
    return len(a) - r


def lo_seek(a,x):
    r = len(a) - 1
    l = 0
    while True:
        m = (r + l) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
        if r == l:
            if a[l] > x:
                l -= 1
            if -1 != l:
                if a[l] == x:
                    l -= 1
            break
    return l + 1


def merge_sort(a):
    if len(a) <= 1:
        return a
    cut = len(a) // 2
    return merger(merge_sort(a[:cut]), merge_sort(a[cut:]))


def merger(a, b):
    out = []
    while len(a) * len(b) > 0:
        if a[0] <= b[0]:
            out.append(a[0])
            del a[0]
        else:
            out.append(b[0])
            del b[0]
    out.extend(a)
    out.extend(b)
    return out

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
