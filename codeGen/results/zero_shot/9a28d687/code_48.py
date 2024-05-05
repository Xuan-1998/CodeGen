n = int(input())  # read n
costs = list(map(int, input().split()))  # read costs
strings = [input() for _ in range(n)]  # read strings

sorted_strings = sorted(strings)

total_cost = 0
for s in sorted_strings:
    total_cost += len(s)  # add the cost of reversing the string

print(total_cost)
