def generate_steady_tables(N, M):
    # Initialize the first row with all values set to 0
    table = [[0] * (M - N + 1) for _ in range(N)]

    def recursive_generate(i, total_sum, prev_sum):
        if i == N:
            return [table]
        else:
            result = []
            for j in range(M - N + 2):
                new_table = table.copy()
                new_table[i] = [prev_sum + k for k in range(j, M - N + j)]
                result.extend(recursive_generate(i + 1, total_sum + sum(new_table[i]), sum(new_table[i])))
            return result

    return recursive_generate(0, 0, 0)

# Test the function
N, M = map(int, input().split())
print(len(generate_steady_tables(N, M)) % 1000000000)
