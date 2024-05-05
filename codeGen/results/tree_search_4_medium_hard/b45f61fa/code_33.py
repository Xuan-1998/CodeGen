code
def matrix_chain_order(p):
    n = len(p)
    m = [[0] * (n+1) for _ in range(n+1)]

    for chain_len in range(2, n+1):
        for start_matrix in range(n-chain_len+1):
            end_matrix = start_matrix + chain_len
            min_cost = float('inf')
            for split_matrix in range(start_matrix+1, end_matrix):
                cost = m[start_matrix][split_matrix-1] + p[start_matrix]*p[split_matrix]*p[end_matrix] + m[split_matrix][end_matrix]
                if cost < min_cost:
                    min_cost = cost
                    m[start_matrix][end_matrix] = cost

    order = []
    chain_len = n-1
    start_matrix = 0
    while chain_len > 1:
        end_matrix = next((i for i in range(chain_len, start_matrix-1, -1) if m[start_matrix][i] == min_cost), None)
        order.append('(' + chr(ord('A')+start_matrix) + ')' if start_matrix != 0 else '')
        order.append(chr(ord('A')+end_matrix))
        order.append(')')
        start_matrix = end_matrix
        chain_len -= 1

    return ''.join(order)

p = list(map(int, input().split()))
print(matrix_chain_order(p))
