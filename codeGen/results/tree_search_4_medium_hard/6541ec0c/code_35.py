code = []

n, k = map(int, input().split())
values = list(map(int, input().split()))
memo = {}

for i in range(n):
    memo[i] = {}
    for j in range(k+1):
        memo[i][j] = False

def dfs(i, parent, xor_val):
    if i in memo:
        return
    values_at_node = [values[i]]
    for child in range(len(values)):
        if child != parent and values[child] ^ values_at_node[0] == xor_val:
            values_at_node.append(values[child])
    if len(set(values_at_node)) == 1:
        memo[i][k-1] = True
    else:
        for j in range(k, 0, -1):
            if memo[parent].get(j) and set(values_at_node) == {values_at_node[0]}:
                memo[i][j-1] = True

for i in range(1, n):
    dfs(i, 0, values[i-1])

print("YES" if any(memo[i].get(k) for i in range(n)) else "NO")
