def min_reverse_cost(strings):
    n = len(strings)
    cost = 0
    for i in range(n):
        prev_min_cost = cost
        if strings[i] != ''.join(reversed(strings[i])):
            cost += strings[i].count('1')
        else:
            cost = prev_min_cost
    return -1 if cost == prev_min_cost else cost

n = int(input())
costs = [int(input()) for _ in range(n)]
strings = [input() for _ in range(n)]
print(min_reverse_cost(strings))
