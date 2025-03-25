# riesene technikou monotonic stack
# upravene riesenie ulohy najdenia najblizsieho vacsieho cisla
# hladame prvok pred najblizsim vacsim cislom (preto ta uprava indexov)
# a pozerame oba smery, preto to iste dvakrat (rozdiel je v uprave indexov)
# deque pouzivame ako stack, pop a stack[-1] by mali byt O(1)

from collections import deque

n = input()
arr = list(map(int, input().split(" ")))

stack = deque()
result1 = [None] * len(arr)

# direction >
for i in reversed(range(len(arr))):

    while (len(stack) != 0 and stack[-1][1] <= arr[i]):
        stack.pop()

    if (len(stack) == 0):
        result1[i] = len(arr)
    else:
        result1[i] = stack[-1][0] # storing the index of the nearest larger / equal value
        
    result1[i] = max(0, result1[i] - i - 1)

    stack.append((i,arr[i]))

stack = deque()

# staci uz len cislo a rovno budeme printovat
result2 = None

# direction <
for i in range(0, len(arr)):
    while (len(stack) != 0 and stack[-1][1] <= arr[i]): # including equals, because stack cannot grow with equal numbers
        stack.pop()

    if (len(stack) == 0):
        result2 = -1
    else:
        result2 = stack[-1][0] # storing the index of the nearest larger / equal value
    
    # uprava pre nase potreby - hra s indexami
    result2 = max(0, i - result2 - 1)

    if (result1[i] == result2): print("=", end="")
    if (result1[i] > result2): print(">", end="")
    if (result1[i] < result2): print("<", end="")
    
    stack.append((i,arr[i]))

print()