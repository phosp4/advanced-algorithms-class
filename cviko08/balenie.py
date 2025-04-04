# chyba - body vs body.sorted() - pozor s cim pracujem, nebola to kopia

# horna cast obalu
def treba_vyhodit_hore(b1, b2, b3):
    return (b3[1] - b2[1]) * (b2[0] - b1[0]) > (b2[1] - b1[1]) * (b3[0] - b2[0])

# dolna cast obalu
def treba_vyhodit_dole(b1, b2, b3):
    return (b3[1] - b2[1]) * (b2[0] - b1[0]) < (b2[1] - b1[1]) * (b3[0] - b2[0])

# shoelace formula
def najdi_obsah(body):
    total = (body[-1][0] * body[0][1]) - (body[-1][1] * body[0][0])

    for i in range(0, len(body) - 1):
        total += (body[i][0] * body[i+1][1] - body[i][1] * body[i+1][0])
    
    return abs(total) / 2

##### nacitanie

pocet_sad = int(input())

for s in range(pocet_sad):
    n = int(input())
    body = [tuple(map(int, input().split(" "))) for _ in range(n)]

    ##### najdenie obalu

    obsah_vnutra = najdi_obsah(body) # POZOR - musi byt pred sortingom
    body.sort() # sortuje primarne podla prveho

    obal_h = []
    obal_d = []

    for i in range(0, n):

        # tu riesime hornu cast
        while(len(obal_h) > 1 and treba_vyhodit_hore(obal_h[-2], obal_h[-1], body[i])):
            obal_h.pop() # vyhodime stredny bod
        obal_h.append(body[i])

        # tu riesime dolnu cast
        while(len(obal_d) > 1 and treba_vyhodit_dole(obal_d[-2], obal_d[-1], body[i])):
            obal_d.pop()
        obal_d.append(body[i])
    
    ##### najdenie obsahov
    obal = obal_h + (obal_d[1:-1][::-1])
    print((1 - (obsah_vnutra / najdi_obsah(obal))) * 100)