# Receive input
n = int(input())
M = list(map(int, input().split()))

# Initialize variables
ways = 1
prev_m = M[0]
count_map = {1: 1}

for m in M[1:]:
    if m == prev_m:
        ways *= count_map.get(m, 0)
    else:
        ways += count_map.get(prev_m, 0)
    count_map[m] = count_map.get(m, 0) + 1
    prev_m = m

print(ways % (10**9 + 7))
