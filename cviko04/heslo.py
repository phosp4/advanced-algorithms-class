# reasoning:
#   prakticky si vieme presne predstavit strom volani, pocet listov bude logicky n
#   postup - ako keby sme na listy dali premenne a potom namiesto porovnavania len brali porovnavace a podla toho skladali
#   teda staci na par miestach upravit existujuci kod, velmi pekne a stylove
#   predpokladam ze by sa nejako chytro dalo vyhnut vytvaraniu pola result
#   taktiez lepsiu priestorovu zlozitost dosiahnut nahradenim arr1 = arr1[1:] za pomocne premenne i, j

n = int(input())
syms = list(input()[::-1])

def merge_sort_back(arr) :
    n = len(arr)
    if n <= 1 :
        return arr
    mid = n//2
    return merge_by_syms(merge_sort_back(arr[:mid]), merge_sort_back(arr[mid:]))

def merge_by_syms(arr1, arr2) :
    result = []
    while (len(arr1) > 0) and (len(arr2) > 0) :

        symbol = syms.pop()

        if symbol == '<' :
            result.append(arr1[0])
            arr1 = arr1[1:]
        else:
            result.append(arr2[0])
            arr2 = arr2[1:]
            
    # doplnenie zvysku
    result.extend(arr1)
    result.extend(arr2)
    return result

order = merge_sort_back([i for i in range(1,n+1)])

result = [0]*n

for i, ord in enumerate(order):
    result[ord-1] = i+1

print(" ".join(map(str, result)))