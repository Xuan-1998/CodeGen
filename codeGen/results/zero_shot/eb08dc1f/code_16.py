n = int(input())
num_blocks = [0] * (n + 1)
for i in range(10**n):
    str_i = str(i).zfill(n)
    for j in range(len(str_i)):
        block_len = 1
        while j + block_len < len(str_i) and str_i[j] == str_i[j + block_len]:
            block_len += 1
        num_blocks[block_len] += 1
print(*[num % 998244353 for num in num_blocks], sep=' ')
