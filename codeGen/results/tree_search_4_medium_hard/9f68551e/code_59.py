import sys

def min_mana(n):
    monsters = [int(x) for x in input().split()]
    states = [0] * n
    for i in range(n-1, -1, -1):
        if monsters[i] <= i+1:
            states[i] = monsters[i]
        else:
            states[i] = max(states[i+1], monsters[i] - (i+1)) + i+1
    return states[0]

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_mana(n))
