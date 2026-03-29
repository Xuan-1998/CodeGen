def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(i):
            m[j][i] = float('inf')
            for k in range(j, i):
                q = m[j][k] + m[k + 1][i] + p[j] * p[k] * p[i]
                if q < m[j][i]:
                    m[j][i] = q

    s = [""] * (n - 1)
    i, j = n - 2, 0
    while j >= 0:
        if j + 1 < n and m[j][n - 1] == m[j + 1][n - 1]:
            j -= 1
        else:
            s[i] = "(" + s[j + 1]
            for k in range(j, i):
                s[k] = ")(" + s[k]
            s[i] += ")"
            i -= 1
            j -= 1

    return "".join(s)

if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    print(matrix_chain_order(p))
