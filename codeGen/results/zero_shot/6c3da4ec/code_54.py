import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_val = 0
max_bin = ''

for i in range(n):
    for j in range(i+1, n):
        substr1 = s[i:j]
        if substr1:  # non-empty substring
            for k in range(j+1, n):
                substr2 = s[j:k]
                if substr2:  # non-empty substring
                    or_result = int(substr1, 2) | int(substr2, 2)
                    max_val = max(max_val, or_result)
                    max_bin = bin(max_val)[2:]

print(max_bin.zfill(n))  # print the maximum value in binary representation without leading zeroes
