import sys
from collections import namedtuple

Matrix = namedtuple('Matrix', 'rows cols')

def read_matrices():
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.read().split()]
    return [Matrix(rows=p[i], cols=p[i+1]) for i in range(n-1)]

def dp(table, matrices):
    n = len(matrices)
    for length in range(2, n):
        for i in range(n-length):
            j = i + length - 1
            table[i][j] = float('inf')
            for k in range(i, j):
                cost = (matrices[i].rows * matrices[k].cols *
                        matrices[k+1].cols)
                if cost < table[i][j]:
                    table[i][j] = cost
    return table

def main():
    matrices = read_matrices()
    n = len(matrices)
    dp_table = [[float('inf')] * (n-1) for _ in range(n-1)]
    dp_table = dp(dp_table, matrices)

if __name__ == '__main__':
    main()
