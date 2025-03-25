def velkost_makovnika():
    # reading from the input
    k, n = map(int, input().split(" "))
    p = [0]*k
    for i in range(k):
        p[i] = int(input())

    # k = 2
    # n = 16
    # p = [7, 8]

    # calculation

    # prechadzaj najvacsimi moznymi kusmi, od najvacsieho
    for piece_size in range(max(p),0, -1): # 8, 7, 6, 5, 4, 3, ...

        c = 0

        # prechadzaj makovnikmi
        for i in range(len(p)): # 0, 1, 2, 3, 4, ...

            c += p[i] // piece_size
            # rest += p[i] % piece_size

            if (c >= n):
                print(piece_size)
                print(sum(p) - piece_size*n)
                return
    
    print("0")
    print(sum(p))

velkost_makovnika()