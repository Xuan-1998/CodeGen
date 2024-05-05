n = int(input())
s = input()
max_possible = 0

for i in range(n):
    if s[i] == '1':
        start_val = [0]
        for j in range(i, n):
            start_val.append(max(start_val[-1], int(s[j])) + 1)
        max_start = 0
        for k in range(len(s) - i - 1):
            max_start = max(max_start, start_val[k])
        max_possible = max(max_possible, max_start + sum(1 for x in s[i:] if x == '1'))

print(bin(max_possible)[2:])
