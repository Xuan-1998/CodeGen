code
n = int(input())
s = input()

ones = [i for i in range(n) if s[i] == '1']
zeros = [i for i in range(n) if s[i] == '0']

max_or = 0

# Take two substrings: one from the beginning and one from the end
for i in range(len(ones)):
    for j in range(len(zeros)):
        or_val = int(''.join([s[ones[i]], s[zeros[j]]]), 2)
        max_or = max(max_or, or_val)

print(bin(max_or)[2:].zfill(n).lstrip('0') or '0')
