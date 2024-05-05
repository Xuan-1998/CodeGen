def gen_binary_representations(n):
    representations = []
    for i in range(n+1):
        bin_i = bin(i)[2:]  # [2:] to remove the '0b' prefix
        representations.append(bin_i)
    return representations

def has_consecutive_ones(bin_i):
    for i in range(len(bin_i)-1):
        if bin_i[i] == '1' and bin_i[i+1] == '1':
            return True
    return False

n = int(input())
representations = gen_binary_representations(n)
ans = 0
for bin_i in representations:
    if not has_consecutive_ones(bin_i):
        ans += 1
print(ans)
