n = int(input())
s = input()
a = [int(x) for x in input().split()]
ways = 0
max_length = 0
min_substrings = float('inf')

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        substring = s[i - 1:j]
        valid = True
        for k, char in enumerate(substring):
            if char.isalpha() and k > a[ord(char) - ord('a')]:
                valid = False
                break
        if valid:
            ways += 1

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        substring = s[i - 1:j]
        if len(substring) > max_length:
            max_length = len(substring)
        min_substrings = min(min_substrings, j - i + 1)

print(ways % (10**9 + 7))
print(max_length)
print(min_substrings)
