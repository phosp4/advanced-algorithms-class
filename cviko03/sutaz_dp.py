n = int(input())
lists = []

for i in range(3):
    line = input().split()
    list_x = [int(line[j]) for j in range(n)]
    lists.append(list_x)

def find_min_sum(i1, i2, i3):

    list_a = lists[i1]
    list_b = lists[i2]
    list_c = lists[i3]

    dp0 = [None] * n
    dp1 = [float('inf')] * n
    dp2 = [float('inf')] * n

    dp0[0] = list_a[0]
    
    for i in range(1, n):
        dp0[i] = list_a[i] + dp0[i - 1]
        dp1[i] = list_b[i] + min(dp0[i - 1], dp1[i - 1])
        dp2[i] = list_c[i] + min(dp1[i-1], dp2[i-1]) if i>1 else dp2[i]

    # vrat idx ktory "vybublal" vpravo dole
    return dp2[-1]

perms = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
print(min(find_min_sum(*idxs) for idxs in perms))