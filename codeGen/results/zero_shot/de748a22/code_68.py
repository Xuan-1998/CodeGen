def read_input():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        signs = list(map(lambda x: 1 if x == '+' else -1, input()))
        queries = [list(map(int, input().split())) for _ in range(q)]
        yield n, q, signs, queries

def update_bit(bit_array, index, value):
    while index < len(bit_array):
        bit_array[index] += value
        index += (index & -index)

def query_bit(bit_array, index):
    sum = 0
    while index > 0:
        sum += bit_array[index-1]
        index -= (index & -index)
    return sum

for n, q, signs, queries in read_input():
    prefix_sum_signs = [0] * (n + 1)
    total_sum_signs = sum(signs)

    for i in range(n):
        update_bit(prefix_sum_signs, i+1, signs[i])

    for l, r in queries:
        sign_variable_sum_left = query_bit(prefix_sum_signs, l-1) if l > 0 else 0
        sign_variable_sum_right = query_bit(prefix_sum_signs, r) - (query_bit(prefix_sum_signs, l-1) if l > 0 else 0)
        result = min(abs(total_sum_signs + sign_variable_sum_left), abs(total_sum_signs + sign_variable_sum_right))
        print(result)
