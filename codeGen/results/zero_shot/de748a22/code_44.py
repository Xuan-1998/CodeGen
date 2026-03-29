def process_input():
    n, q = map(int, input().split())
    arr = list(input())
    return n, q, arr

n, q, arr = process_input()

cum_sum = [0]
sign_sum = 0
for x in arr:
    sign_sum += x
    cum_sum.append(sign_sum)

def query(l, r):
    return (cum_sum[r] - cum_sum[l-1]) // abs((cum_sum[r] - cum_sum[l-1])) * abs((cum_sum[r] - cum_sum[l-1]))

for _ in range(q):
    l, r = map(int, input().split())
    print(query(l, r))
