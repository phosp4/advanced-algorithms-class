# ofc chyby co boli tak len hlupe, indexy, o jednotku, atd...
# inspiracia: https://www.youtube.com/watch?v=xztU7lmDLv8

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
def get_tree_max(start, end):
    global max_tree
    start += len(max_tree) // 2
    end += len(max_tree) // 2
    max_val = float('-inf')

    while (start < end): # asi =?
        if start % 2 == 1:
            max_val = max(max_val, max_tree[start])
            start += 1
        if end % 2 == 1:
            end -= 1
            max_val = max(max_val, max_tree[end])
        
        start = start // 2
        end = end // 2

    return max_val

# get max / min
def get_tree_min(start, end):
    global min_tree
    start += len(min_tree) // 2
    end += len(min_tree) // 2
    min_val = float('inf')

    while (start < end): # asi =?
        if start % 2 == 1:
            min_val = min(min_val, min_tree[start])
            start += 1
        if end % 2 == 1:
            end -= 1
            min_val = min(min_val, min_tree[end])
        
        start = start // 2
        end = end // 2

    return min_val


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
        outs.append([get_tree_min(int(inp[1]) - 1, int(inp[2])), get_tree_max(int(inp[1]) - 1, int(inp[2]))])
    if (inp[0] == '.'):
        update_tree_value(int(inp[1]) - 1, int(inp[2]))
    inp = input()

for tuple in outs:
    print(tuple[0], tuple[1])