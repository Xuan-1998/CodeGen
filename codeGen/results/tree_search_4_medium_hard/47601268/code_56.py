def has_consecutive_ones(i):
    bin_i = bin(i)[2:]
    for i in range(len(bin_i) - 1):
        if bin_i[i] == '1' and bin_i[i + 1] == '1':
            return True
    return False

n = int(input())
dp_state = [True]
for i in range(1, n + 1):
    if not has_consecutive_ones(i):
        dp_state.append(True)
    else:
        dp_state.append(dp_state[-1])
print(sum(dp_state) - 1)
