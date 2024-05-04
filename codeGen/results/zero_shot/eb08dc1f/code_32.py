n = int(input())
num_list = []
for i in range(10**n):
    num_list.append(str(i).zfill(n))

block_counts = {}
for num in num_list:
    block_len = 1
    while len(num) > block_len:
        if num[block_len - 1] == num[block_len:]:
            block_len += 1
        else:
            break
    block_counts[block_len] = block_counts.get(block_len, 0) + 1

print(*[f"{count % 998244353}" for count in block_counts.values()], sep=' ')
