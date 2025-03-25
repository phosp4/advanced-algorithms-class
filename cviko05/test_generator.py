# n = 50000
# max_val = 100
# commands = 5

n = 500000
max_val = 1000000000
commands = 500000

file = open("input.txt", "w")

file.write(str(n) + "\n")

from random import *
for i in range(0, n):
    file.write(str(randint(0, max_val)))
    if i != n-1: file.write(" ")

for i in range(0,commands):
    what = randint(0,1)
    if what == 0:
        idx = randint(1,n)
        new_num = randint(1, max_val)
        file.write("\n." + " " + str(idx) + " " + str(new_num))
    else:
        od = randint(1, n)
        do = randint(od, n)
        file.write("\n?" + " " + str(od) + " " + str(do))
    
file.write("\n-")
file.close()