# Step 1: Understand the problem
# The goal is to find the maximum possible distribution index of the tree.

# Step 2: Define the variables and data structures needed for this problem.
n = int(input())  # number of nodes in the tree
edges = []  # list of edges in the tree
m = int(input())  # number of prime factors of k
primes = []  # list of prime numbers

# Step 3: Read the input and store it in variables.
for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

for _ in range(m):
    p = int(input())
    primes.append(p)

k = prod(primes)  # calculate k as the product of all prime numbers

# Step 4: Calculate the maximum possible distribution index.
def dfs(node, parent):
    total = 1
    for edge in edges:
        if edge[0] == node and edge[1] != parent:
            total *= edge[1]
        elif edge[0] == node and edge[1] == parent:
            continue
        elif edge[1] == node and edge[0] != parent:
            total *= edge[0]
        elif edge[1] == node and edge[0] == parent:
            continue
    return total

def distribution_index():
    index = 0
    for i in range(2, n):
        if dfs(i, 1) % k == 0:
            index += (n - 1) * log(dfs(i, 1), k)
    return index

print(distribution_index() % (10**9 + 7))
