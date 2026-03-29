# Step 1: Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Step 2: Initialize variables
total_cost = 0
sorted_strings = [''] * n

# Step 3: Sort the strings using only the operation of reversing a string
for i in range(n):
    cost = costs[i]
    if not sorted_strings[i]:
        total_cost += cost
        for j in range(len(strings[i])):
            c = strings[i][j]
            while c in strings:
                cost -= 1
                c = c[::-1]
            sorted_strings[i] += c
    else:
        for j in range(n):
            if not sorted_strings[j]:
                total_cost += costs[j]
                sorted_strings[j] = strings[j][::-1]
                break

# Step 4: Check if the strings are lexicographically sorted
for i in range(1, n):
    while len(sorted_strings[i-1]) < len(sorted_strings[i]):
        sorted_strings[i-1] += sorted_strings[i][-1]
        sorted_strings[i] = sorted_strings[i][:-1]

sorted_strings.sort()
total_cost -= sum(costs)

# Step 5: Print the result
if ''.join(sorted_strings) == ''.join(sorted(strings)):
    print(total_cost)
else:
    print(-1)
