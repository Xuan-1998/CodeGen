import sys
n = int(sys.stdin.readline())
count = [0] * (n + 1)
for num in range(10**n):
    digits = str(num).zfill(n)
    block_length = 1
    for i in range(1, n):
        if digits[i] == digits[i - 1]:
            block_length += 1
        else:
            count[block_length] += 1
            block_length = 1
    count[block_length] += 1

print(*count, sep=' ')
