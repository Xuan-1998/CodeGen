n = int(input())
dp_state = [False] * (n + 1)
for i in range(2**n):
    bin_num = bin(i)[2:].zfill(n)
    has_consecutive_ones = False
    for j in range(len(bin_num) - 1):
        if bin_num[j] == '1' and bin_num[j+1] == '1':
            has_consecutive_ones = True
            break
    dp_state[i] = not has_consecutive_ones
result = sum(dp_state)
print(result)
