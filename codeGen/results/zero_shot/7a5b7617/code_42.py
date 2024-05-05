def generate_tables(N, M):
    if N == 0 or M == 0:
        return [[]]
    
    tables = []
    for row in generate_tables(N-1, M):
        for i in range(M+1):
            new_row = [i] * (N-1) + [M - sum(row)]
            tables.append(new_row)
    
    return tables

def count_stable_tables(N, M):
    tables = generate_tables(N, M)
    stable_tables = []
    for table in tables:
        is_stable = True
        for i in range(2, N+1):
            if sum(table[:i]) < sum(table[i-1:i]):
                is_stable = False
                break
        if sum(table) <= M and is_stable:
            stable_tables.append(table)
    
    return len(stable_tables)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_stable_tables(N, M) % 1000000000)
