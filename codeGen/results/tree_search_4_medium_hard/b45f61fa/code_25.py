def matrix_chain_order(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n+1):
        i = 0
        while i < n - length + 1:
            j = i + length - 1
            min_cost = float('inf')
            k = i
            while k <= j:
                cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if cost < min_cost:
                    min_cost = cost
                k += 1
            m[i][j] = min_cost
            i += 1

    return build_order(m, n)

def build_order(m, n):
    order = []
    i = j = 0
    while j < n-1:
        if i+1 == j:
            order.append('A' + str(i))
            i += 1
        else:
            k = i
            min_cost = float('inf')
            while k <= j:
                cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j]
                if cost < min_cost:
                    min_cost = cost
                    split_index = k
                k += 1
            order.append('(')
            order.append('A' + str(i))
            order.append(')')
            for _ in range(split_index-i):
                order.append('(')
                order.append('A')
                i += 1
            order.append(')')
        j += 1

    return ''.join(order)

p = list(map(int, input().split()))
print(matrix_chain_order(p))
