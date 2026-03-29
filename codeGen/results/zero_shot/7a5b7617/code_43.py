code
import sys

def generate_tables(n, m):
    # Generate all possible tables of size n x m
    tables = []
    for i in range(m**n):
        table = [0] * (n+1)
        for j in range(n):
            table[j+1] += 1 if (i >> j) & 1 else 0
        tables.append(table)

    return tables

def count_steady_tables(tables, n, m):
    # Filter out tables that don't satisfy the conditions
    steady_tables = []
    for table in tables:
        if all(sum(table[:j+1]) >= sum(table[:i]) for j in range(1, n)) and sum(table) <= m:
            steady_tables.append(table)

    return len(steady_tables)

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        tables = generate_tables(N, M)
        num_steady_tables = count_steady_tables(tables, N, M)
        print(num_steady_tables % 1000000000)

solve()
