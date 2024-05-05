signs = []
queries = []
total_sum = 0
pos_count = 0
neg_count = 0

n, q = map(int, input().split())
for _ in range(n):
    sign = input().strip()
    if sign == "+":
        signs.append(1)
        pos_count += 1
    else:
        signs.append(-1)
        neg_count += 1
    total_sum += signs[-1]

for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

def process_query(l, r):
    left_sum = 0
    right_sum = 0
    pos_count_l = pos_count
    neg_count_l = neg_count
    for i in range(l-1, -1, -1):
        left_sum += signs[i]
        if signs[i] > 0:
            pos_count_l -= 1
        else:
            neg_count_l -= 1

    for i in range(r, n):
        right_sum += signs[i]
        if signs[i] > 0:
            pos_count_l += 1
        else:
            neg_count_l += 1

    target_sum = left_sum + right_sum
    pos_diff = abs(target_sum) - (pos_count_l - neg_count_l)
    return min(pos_diff, n - r - l + 1)

for query in queries:
    l, r = query
    print(process_query(l, r))
