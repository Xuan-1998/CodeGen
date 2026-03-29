from sys import stdin, stdout

n = int(stdin.readline())
num_list = []

for _ in range(n):
    num = 0
    for __ in range(10**_):
        num = (num * 10 + 1) % (10**_)  
        num_list.append(str(num).zfill(_))  

block_counts = [0] * n
for num in num_list:
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            block_counts[i] += 1

stdout.write(' '.join(map(str, [x % 998244353 for x in block_counts])) + '\n')

