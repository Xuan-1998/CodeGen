def find_eating_order(n, a, k, b):
    i = j = 0
    actions = []
    while i < n and j < k:
        weight = a[i]
        actions_part = []
        while weight < b[j] and i < n - 1:
            i += 1
            weight += a[i]
            actions_part.append((i, 'L'))
        if weight != b[j]:
            return "NO", []
        actions.extend(reversed(actions_part))
        i += 1
        j += 1
    if j != k:
        return "NO", []
    return "YES", actions

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))
k = int(input().strip())
b = list(map(int, input().strip().split()))

# Process and output
result, actions = find_eating_order(n, a, k, b)
print(result)
if result == "YES":
    for action in actions:
        print(action[0], action[1])
