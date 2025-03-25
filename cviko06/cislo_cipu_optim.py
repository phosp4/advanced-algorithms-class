string, n = input(), int(input())
ins = [int(input()) for _ in range(n)]

base = len(string)
for in_num in ins:

    result = []
    remainder = in_num

    while in_num>0:
        in_num -= 1
        remainder = in_num % base
        result.append(string[remainder])
        in_num //= base

    print(''.join(result[::-1]))