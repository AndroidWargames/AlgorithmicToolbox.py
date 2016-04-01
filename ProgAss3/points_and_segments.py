# Uses python3
import sys
import time
import random

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts = randomized_quick_sort(starts, 0, len(ends)-1)
    ends = randomized_quick_sort(ends, 0, len(ends)-1)
    for i in range(len(points)):
        p = points[i]
        s = hi_seek(starts, p)
        e = lo_seek(ends, p)
        cnt[i] = len(starts) - s - e
    return cnt


def hi_seek(a, x):
    r = len(a) - 1
    l = 0
    if r == l:
        if x <= a[0]:
            return 1
        else:
            return 0
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


def lo_seek(a, x):
    r = len(a) - 1
    l = 0
    if r == l:
        if x >= a[0]:
            return 1
        else:
            return 0
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

def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    random.seed(25)
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1)
    randomized_quick_sort(a, m[1] + 1, r)
    return a


def partition3(a, l, r):
    x = a[l]
    j, k = l, l
    for i in range(l+1, r + 1):
        if a[i] < x:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
            if j != k:
                a[i], a[k] = a[k], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]
    return [j, k]


def quick_timer(a):
    z = time.time()
    randomized_quick_sort(a,0,len(a)-1)
    return time.time() - z

def merge_timer(a):
    z = time.time()
    merge_sort(a)
    return time.time() - z


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