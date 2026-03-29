n = int(input())
s = input()

substrings = []
for i in range(n):
    for j in range(i+1, n+1):  # consider substrings ending at index j
        substrings.append(s[i:j])

or_values = {}
for i in range(len(substrings)):
    for j in range(i+1, len(substrings)):
        or_value = int(substrings[i], 2) | int(substrings[j], 2)
        or_values[or_value] = or_values.get(or_value, 0) + 1

max_or_value = max(or_values.keys())
print(bin(max_or_value)[2:].zfill(n).lstrip('0'))
