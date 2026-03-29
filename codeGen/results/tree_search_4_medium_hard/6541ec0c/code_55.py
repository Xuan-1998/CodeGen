import sys

def recursive_function(i, j, xor_val, k):
    if dp[i][j][xor_val]:
        return 1
    for child in children[i]:
        if child != -1:
            if (child < k and xor_val == XOR[child]) or \
               (child >= k and xor_val == 0):
                continue
            if recursive_function(child, j-1, xor_val ^ node_values[child], k) == 1:
                dp[i][j][xor_val] = 1
                return 1

def solve():
    global dp, children, XOR, node_values, n, k
    dp = [[[0] * (10**9 + 1)] * (n + 1)] * (k + 1)
    children = [-1] * n
    XOR = [0] * n
    node_values = [0] * n
    n, k = map(int, input().split())
    for _ in range(n-1):
        u, v = map(int, input().split())
        children[u-1] = v-1
        children[v-1] = u-1
    node_values = list(map(int, input().split()))
    answer = "YES"
    for i in range(n-1, -1, -1):
        for j in range(1, n+1):
            for xor_val in range(10**9 + 1):
                if recursive_function(i, j, xor_val, k) == 1:
                    answer = "NO"
                    break
    print(answer)

if __name__ == "__main__":
    solve()
