n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(m):
    queries.append(list(map(int, input().split())))

state = [[[0, 0]] for _ in range(n+1)]

for i in range(1, n+1):
    state[i][i-1] = [0, 0]
for i in range(1, n+1):
    for j in range(i, n+1):
        if array[j-1] >= array[j]:
            state[i][j][0] = max(state[i-1][k][0] for k in range(j-i+2) if array[k-1] > array[k]) + 1
        else:
            state[i][j][1] = max(state[i-1][k][1] for k in range(j-i+2) if array[k] <= array[k+1]) + 1

for l, r in queries:
    print("Yes" if state[n][r][0] > state[n][r][1] else "No")
