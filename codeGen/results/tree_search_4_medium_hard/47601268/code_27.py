import sys

n = int(sys.stdin.readline())

dp_state = [False] * (n + 1)
for i in range(1, n + 1):
    bin_i = bin(i)[2:]
    has_consecutive_ones = False
    for j in range(len(bin_i) - 1):
        if bin_i[j] == '1' and bin_i[j + 1] == '1':
            has_consecutive_ones = True
            break
    dp_state[i] = not has_consecutive_ones

count = sum(dp_state)
print(count)
