n = int(input())
lists = [list(map(int, input().split())) for _ in range(3)]

def compute_min_sum(i1, i2, i3):
    list_a, list_b, list_c = lists[i1], lists[i2], lists[i3]
    
    dp_a = [0] * n
    dp_b = [float('inf')] * n
    dp_c = [float('inf')] * n
    
    # Compute dp_a
    dp_a[0] = list_a[0]
    for i in range(1, n):
        dp_a[i] = dp_a[i - 1] + list_a[i]
    
    # Compute dp_b
    for i in range(1, n):
        dp_b[i] = min(dp_a[i - 1], dp_b[i - 1]) + list_b[i]
    
    # Compute dp_c
    for i in range(2, n):
        dp_c[i] = min(dp_b[i - 1], dp_c[i - 1]) + list_c[i]
    
    return dp_c[-1]

# Generate all permutations of [0, 1, 2] manually
permutations = [
    [0, 1, 2], [0, 2, 1], [1, 0, 2],
    [1, 2, 0], [2, 0, 1], [2, 1, 0]
]

# Try all permutations of list indices and find the minimum sum
min_sum = float('inf')
for perm in permutations:
    min_sum = min(min_sum, compute_min_sum(*perm))

print(min_sum)
