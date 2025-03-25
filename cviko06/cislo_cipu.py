# nacitanie
string = input()
n = int(input())
ins = [None] * n
for i in range(n):
    ins[i] = int(input())

str_len = len(string)
for in_num in ins:

    result = ""
    remainder = in_num

    while in_num>0:
        in_num -= 1
        remainder = in_num % str_len
        result = string[remainder] + result
        in_num //= str_len

    print(result)