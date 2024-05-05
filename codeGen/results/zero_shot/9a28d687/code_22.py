from collections import Counter

n = int(input())  # Read n from standard input
costs = list(map(int, input().split()))  # Read the costs of reversing each string
strings = [input() for _ in range(n)]  # Read the strings

# Count the frequency of characters at each position in all strings
char_freq = Counter()
for s in strings:
    for i, c in enumerate(s):
        char_freq[(i, c)] += 1

total_cost = 0
for i, c in sorted(char_freq):  # Sort by character and position
    if char_freq[(i, c)] > 1:  # If there are multiple strings that end with this character
        for s in strings:
            if s[i:] == str(c) * (n - len(s)):  # Check if the string ends with this character
                total_cost += costs[s.index(str(c)) + i]  # Add the cost of reversing this substring to the total cost
                break

if total_cost > 0:  # If it is possible to sort the strings
    print(total_cost)  # Print the minimum total cost required to sort the strings in lexicographical order
else:
    print(-1)  # Output -1 if it is impossible to sort the strings
