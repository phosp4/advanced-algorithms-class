# n = 3
# p = [9,9,9]

# pozor na:
#   ci pri velkom vstupe sa nevytvori pole velkej dlzky ktore je zbytocne
#   ci tam nemam nejaku bulharsku konstantu co sa neprisposobi vstupu
#   ci som tam nenechal debugging printy (zbytocne strateny pokus)

k, n = map(int, input().split(" "))
p = [0]*k
for i in range(k):
    p[i] = int(input())

def najdi_velkost(piece_size):
    c = 0

    # prechadzaj makovnikmi
    for i in range(len(p)):
        c += p[i] // piece_size
    
    return c

posledny_vhodny_idx = [-1]

def binary_search(od_idx, po_idx):

    stred_idx = (od_idx + po_idx) // 2

    # dopln hodnotu do pola
    akt_hodnota = najdi_velkost(stred_idx+1)
    # print(s)

    # ak je pole jednoprvkove, koncime
    if ((po_idx-od_idx) <= 1):
        if (akt_hodnota >= n): posledny_vhodny_idx[0] = stred_idx
        return
    else:
        # chod doprava alebo dolava
        if (akt_hodnota >= n):
            # je to dobre, ale mozno existuje lepsie
            posledny_vhodny_idx[0] = stred_idx
            binary_search(stred_idx, po_idx)
        elif (akt_hodnota < n):
            binary_search(od_idx, stred_idx)

binary_search(0, max(p))
print(posledny_vhodny_idx[0]+1)
print(sum(p) - ((posledny_vhodny_idx[0]+1) * n))