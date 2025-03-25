pocet = int(input())
nums = []

for i in range(pocet):
    line = input()
    nums.append(line.split(' '))

for input in nums:
    print(int(input[0]) + int(input[1]))