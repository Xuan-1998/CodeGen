# Read input
n = int(input())
M = list(map(int, input().split()))

# Create a dictionary where keys are elements from M and values are their respective counts.
count_dict = {}
for m in M:
    if m not in count_dict:
        count_dict[m] = 1
    else:
        count_dict[m] += 1

answer = 1
for k, v in count_dict.items():
    answer *= math.comb(v + n - 1, n - 1)
    answer %= 10**9 + 7

print(answer)
