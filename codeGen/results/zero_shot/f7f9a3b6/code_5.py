n = int(input())
s = input()
a = [int(x) for x in input().split()]

total_count = [0] * 26
for i in range(n):
    char = s[i]
    index = ord(char.lower()) - ord('a')
    total_count[index] += 1

ways = 0
longest_length = 0
min_substrings = float('inf')

# ... (rest of the code)

print(ways % (10 ** 9 + 7))
print(longest_length)
print(min_substrings)
