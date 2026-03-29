# Read input
n = int(input())
s = input()
a = list(map(int, input().split()))

# Initialize variables
total_ways = 0
max_length = 0
min_substr_count = n

# Iterate over the string s
for i in range(n):
    # Initialize variables for this substring
    substr_count = 1
    max_consecutive_count = a[ord(s[i]) - ord('a')]
    curr_consecutive_count = 1
    
    # Calculate the maximum consecutive count and substring count for this substring
    for j in range(i+1, n):
        if s[j] == s[i]:
            curr_consecutive_count += 1
            if curr_consecutive_count > max_consecutive_count:
                max_consecutive_count = curr_consecutive_count
                substr_count += 1
        else:
            break
    
    # Update variables based on this substring
    total_ways += (max_consecutive_count + 1) ** (substr_count - 1)
    max_length = max(max_length, max_consecutive_count * substr_count)
    min_substr_count = min(min_substr_count, substr_count)

print(total_ways % (10**9 + 7))
print(max_length)
print(min_substr_count)
