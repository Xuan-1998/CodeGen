import sys

n = int(sys.stdin.readline())

numbers = [int(f"{i:0>{n}}") for i in range(10**n)]

block_counts = {}

for num in numbers:
    str_num = str(num)
    
    for i in range(1, len(str_num)):
        if str_num[i] != str_num[i-1]:
            block_counts.setdefault(i, 0)
            block_counts[i] += 1

for i in range(1, n+1):
    print(block_counts.get(i, 0) % 998244353, end=' ')

