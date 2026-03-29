n, k, c = map(int, input().split())
requests = []
for _ in range(n):
    r_i, p_i = map(int, input().split())
    requests.append((r_i, p_i))

accepted = 0
total_earned = 0
tables_used = []

requests.sort(key=lambda x: x[0], reverse=True)

for i in range(n):
    r_i, p_i = requests[i]
    for j in range(k):
        if c >= r_i:
            accepted += 1
            total_earned += p_i
            tables_used.append(j)
            break

print(accepted, total_earned)
for i in range(accepted):
    request_index = requests[i][0]
    table_index = tables_used[i]
    print(request_index, table_index)
