n = int(input())
s = input()
max_or = 0

substrings = []
for i in range(n):
    for j in range(i + 1, n + 1):
        substring = s[i:j]
        if len(substring) > 0:
            substrings.append(substring)

or_values = []
for i in range(len(substrings)):
    for j in range(i, len(substrings)):
        or_value = int(substrings[i], 2) | int(substrings[j], 2)
        or_values.append(or_value)

max_or = max(or_values)
print(bin(max_or)[2:])
