import itertools

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        steady_tables = []
        for table in generate_tables(N, M):
            if is_steady(table):
                steady_tables.append(table)
        print(count_steady_tables(N, M))

def generate_tables(N, M):
    table_values = list(itertools.product(range(M), repeat=N))
    return [list(map(list, zip(*table))) for table in table_values]

def is_steady(table):
    prev_sum = 0
    for row in table:
        curr_sum = sum(row)
        if curr_sum < prev_sum:
            return False
        prev_sum = curr_sum
    return True

def count_steady_tables(N, M):
    return len(steady_tables) % 1000000000

if __name__ == "__main__":
    solve()
