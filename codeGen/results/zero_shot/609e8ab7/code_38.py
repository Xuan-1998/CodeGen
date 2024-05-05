if __name__ == "__main__":
    n = int(input())  # Read the number of vertices
    p = [int(x) for x in input().split()]  # Read the parents
    l, r = [], []  # Initialize lists for lower and upper bounds

    for i in range(1, n):
        l.append(int(input()))  # Read the lower bound for each vertex
        r.append(int(input()))  # Read the upper bound for each vertex

    min_ops = float('inf')
    for i in range(1, n):
        min_ops = min(min_ops, dfs(i, l[i], r[i]))

    print(min_ops)  # Print the minimum number of operations
