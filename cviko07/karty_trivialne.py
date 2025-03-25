# trivialne riesenie za bod (O(n^2))

n = input()
arr = list(map(int, input().split(" ")))

for i in range(len(arr)):
    # counter_right = 0
    # counter_ = 0

    iter = 1
    # chod smerom doprava
    while((i+iter) < len(arr) and arr[i+iter] <= arr[i]):
        # counter_right += 1
        iter += 1

    iter2 = 1
    while((i-iter2) >= 0 and arr[i-iter2] <= arr[i]):
        # counter_left += 1
        iter2 += 1
    
    # if (i != len(arr) - 1):
    if iter > iter2: print(">", end="")
    if iter < iter2: print("<", end="")
    if iter == iter2: print("=", end="")

print()