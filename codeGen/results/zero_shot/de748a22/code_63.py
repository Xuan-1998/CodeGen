from sys import stdin

def read_int():
    return int(next(stdin))

n = read_int()
q = read_int()
signs = [1 if c == '+' else -1 for c in next(stdin).strip()]

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = sign_sum = signs[i]
    for j in range(i, n):
        sign_sum += signs[j]
        prefix_sum[j + 1] = sign_sum

queries = []
for _ in range(q):
    l, r = map(int, next(stdin).split())
    queries.append((l - 1, r))

answers = []
for query in queries:
    left, right = query
    sum_left = prefix_sum[left]
    sum_right = prefix_sum[right]

    diff = abs(sum_right) - abs(sum_left)
    if diff % 2 == 0:
        answers.append(diff // 2)
    else:
        answers.append(diff // 2 + (1 if sum_right < 0 else 0))

print('\n'.join(map(str, answers)))
