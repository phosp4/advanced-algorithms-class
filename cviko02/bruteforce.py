# uloha: generuj vsetky postupnosti dlzky n s cislami od 1 do k, doplnenie: bez opakovania
# riesenie: pomocou rekurzie, alternativne: cez zoznam a while cyklus

n = 2 #int(input("n: "))
k = 4 #int(input("k: "))

postupnost = [0]*n

def opakuje_sa(zoznam, pokial_idx):
    for i in range(0, pokial_idx):
        for j in range(i+1, pokial_idx):
            if zoznam[i] == zoznam[j]:
                return True
    
    return False

def generuj_postupnost(c):

    # funguje to, ale jednoduchsie by bolo mat priznakove pole
    # a znacit si pre kazde cislo bolo alebo nebolo pouzite
    if (opakuje_sa(postupnost, c)):
        return

    if (c == n):
        print(postupnost)
        return

    for i in range(1,k+1):
        postupnost[c] = i
        generuj_postupnost(c+1)

generuj_postupnost(0)