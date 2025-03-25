from random import *

file = open("input.txt", "w")

n = 10000

for i in range(0,n):
    file.write(str(randint(0,9)) + " ")

file.close()