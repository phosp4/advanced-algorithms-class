n, lists = int(input()), [[int(num) for num in input().split()] for _ in range(3)]

def find_min_sum(a, b, c):
    a_prev, b_prev, c_prev = lists[a][0],float('inf'),float('inf')
    for idx, (a_idx, b_idx, c_idx) in enumerate(zip(lists[a][1:], lists[b][1:], lists[c][1:]), start=1):
        a_prev, b_prev, c_prev = a_idx + a_prev, b_idx + min(a_prev, b_prev), c_idx + min(b_prev, c_prev) if idx>1 else c_prev
    return c_prev

print(min(find_min_sum(*idxs) for idxs in [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]))