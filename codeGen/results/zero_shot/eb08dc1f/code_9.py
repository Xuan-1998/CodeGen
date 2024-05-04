n = int(input())
numbers = []
for i in range(10**n):
    numbers.append(str(i).zfill(n))

block_counts = {}
for num in numbers:
    for i in range(1, n+1):
        if len(set(num[i-1:i])) == 1:  # Check if all digits are equal
            block_counts[i] = block_counts.get(i, 0) + 1

print(*[block_counts.get(i, 0) % 998244353 for i in range(1, n+1)], sep=' ')
