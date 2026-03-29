import itertools

def count_steady_tables():
    T = int(input())  # Read the number of test cases from stdin

    for _ in range(T):
        N, M = map(int, input().split())  # Read the size of the table from stdin
        tables = []  # Initialize an empty list to store all possible tables

        for row in itertools.product(range(M), repeat=N):
            table = [row]  # Construct a 2D list representing the table
            tables.append(table)

        count = 0  # Initialize the count of steady tables to 0

        for table in tables:
            is_steady = True  # Assume the table is steady initially

            for i, row in enumerate(table):
                if i > 0 and sum(row) < sum(table[i-1]):
                    is_steady = False
                    break

            if is_steady and sum(row) <= M:
                count += 1  # Increment the count of steady tables

        print(count % (10**9 + 7))  # Print the answer modulo 1 000 000 000

count_steady_tables()
