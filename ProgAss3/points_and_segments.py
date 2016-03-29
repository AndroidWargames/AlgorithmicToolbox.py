# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    m = pair_merge_sort(starts, ends)
    starts, ends = m
    for i in range(len(points)):
        f = 0
        p = points[i]
        s = endseeker(starts,p)

        while f < s:
            if p <= ends[f]:
                cnt[i] += 1
            f += 1
    return cnt

def endseeker(a,x):
    l = 0
    r = len(a) - 1
    while l < r:
        m = (r + l) // 2
        if a[m] < x:
            l = m + 1
        elif a[m] > x:
            r = m - 1
        else:
            r = m
    if r < 0:
        return 0
    if l >= len(a):
        return len(a)
    if r == l:
        if a[r] <= x:
            return r + 1
        else:
            return r
    elif a[m] > x:
        return m
    else:
        return m + 1



def pair_merge_sort(a, b):
    if len(a) <= 1:
        return [a, b]
    cut = len(a) // 2
    return pair_merger(pair_merge_sort(a[:cut],
                                       b[:cut]),
                       pair_merge_sort(a[cut:],
                                       b[cut:])
                       )


def pair_merger(a, b):
    sa, sb, ta, tb = a[0], b[0], a[1], b[1]
    out = [[], []]
    while len(sa) > 0 and len(sb) > 0:
        if sa[0] <= sb[0]:
            out[0].append(sa[0])
            out[1].append(ta[0])
            del sa[0]
            del ta[0]
        else:
            out[0].append(sb[0])
            out[1].append(tb[0])
            del sb[0]
            del tb[0]
    out[0].extend(sa)
    out[0].extend(sb)
    out[1].extend(ta)
    out[1].extend(tb)
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
