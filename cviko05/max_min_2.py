# optimalizovana verzia - bezi o trocha kratsie - get_tree_min_max namiesto osobytnych funkcii, atd

# update value
def update_tree_value(orig_idx, val):
    global min_tree, max_tree

    idx = orig_idx + (len(min_tree) // 2)
    min_tree[idx] = val
    max_tree[idx] = val

    while (idx > 1):
        idx = idx // 2
        new_min_val = min(min_tree[2 * idx], min_tree[(2 * idx) + 1])
        new_max_val = max(max_tree[2 * idx], max_tree[(2 * idx) + 1])

        if min_tree[idx] == new_min_val and max_tree[idx] == new_max_val: break
        
        min_tree[idx] = new_min_val
        max_tree[idx] = new_max_val

# get max / min
def get_tree_min_max(left, right):
    global max_tree, min_tree
    
    l_max = left + len(max_tree) // 2
    r_max = right + len(max_tree) // 2
    max_val = float('-inf')

    l_min = left + len(min_tree) // 2
    r_min = right + len(min_tree) // 2
    min_val = float('inf')

    while (l_max < r_max or l_min < r_min): # asi =?

        # max
        if l_max % 2 == 1:
            max_val = max(max_val, max_tree[l_max])
            l_max += 1
        if r_max % 2 == 1:
            r_max -= 1
            max_val = max(max_val, max_tree[r_max])
        
        l_max = l_max // 2
        r_max = r_max // 2

        # min
        if l_min % 2 == 1:
            min_val = min(min_val, min_tree[l_min])
            l_min += 1
        if r_min % 2 == 1:
            r_min -= 1
            min_val = min(min_val, min_tree[r_min])
        
        l_min = l_min // 2
        r_min = r_min // 2

    return min_val, max_val

n = input()
arr = list(map(int, input().split(" ")))
#arr = [5, 7, 2, 8, 9, 1, 7]

# segment tree creation
min_tree = ([None] * len(arr)) + arr
max_tree = ([None] * len(arr)) + arr

for i in range(len(arr)-1,0,-1):
    min_tree[i] = min(min_tree[2*i], min_tree[(2*i)+1])
    max_tree[i] = max(max_tree[2*i], max_tree[(2*i)+1])

outs = []
inp = input()
while(inp != "-"):
    inp = inp.split(" ")
    if (inp[0] == '?'):
        outs.append(get_tree_min_max(int(inp[1]) - 1, int(inp[2])))
    if (inp[0] == '.'):
        update_tree_value(int(inp[1]) - 1, int(inp[2]))
    inp = input()

for tuple in outs:
    print(tuple[0], tuple[1])