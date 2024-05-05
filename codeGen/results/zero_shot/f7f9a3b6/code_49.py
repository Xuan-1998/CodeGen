# Take input
n = int(input())
s = input()
a = list(map(int, input().split()))

# Initialize variables
ways = 0
max_len = 0
min_substrings = float('inf')

# Define a function to check if the substring fulfills the condition
def fulfill_condition(substring):
    for i in range(26):
        count = 0
        for char in substring:
            if ord(char) - ord('a') == i:
                count += 1
            if count > a[i]:
                return False
    return True

# Define a function to get the number of ways to split the string into substrings that fulfill the condition
def get_ways():
    global ways, max_len, min_substrings
    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            if fulfill_condition(s[j:i]):
                ways += 1
                max_len = max(max_len, i - j)
                min_substrings = min(min_substrings, 1 + (n - i) // (i - j))
    return ways % (10**9 + 7)

print(get_ways())
print(max_len)
print(min_substrings)
