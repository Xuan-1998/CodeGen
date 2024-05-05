n = int(input())
s = input()
substrings = []
for i in range(n):
    for j in range(i+1, n+1):
        substrings.append(s[i:j])

max_or = 0
for substring1 in substrings:
    for substring2 in substrings:
        if substring1 != substring2:  
            num1 = int(substring1, 2)
            num2 = int(substring2, 2)
            or_val = num1 | num2
            max_or = max(max_or, or_val)

max_binary = bin(max_or)[2:]

print(max_binary or '0')
