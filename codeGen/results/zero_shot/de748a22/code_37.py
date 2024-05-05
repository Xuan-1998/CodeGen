code
n, q = map(int, input().split())
signs = list(input())
queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

signs_cum_sum = [0]
for sign in signs:
    if sign == "+":
        signs_cum_sum.append(signs_cum_sum[-1] + 1)
    else:
        signs_cum_sum.append(signs_cum_sum[-1] - 1)

def solve_query(l, r):
    cum_sum = signs_cum_sum[r] - signs_cum_sum[l-1]
    max_val = 0
    for i in range(l-1, r+1):
        if signs_cum_sum[i] >= cum_sum // 2:
            max_val = i
            break
    return max_val

answers = []
for q in queries:
    l, r = q
    answers.append(solve_query(l, r))

print(*answers, sep="\n")

code
