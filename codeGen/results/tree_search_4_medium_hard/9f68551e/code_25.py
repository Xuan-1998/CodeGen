import sys

def min_mana_required(n, ki, h):
    dp = {}
    for i in range(n):
        j = ki[i]
        if j >= max(ki):  # base case: no more monsters after this time
            dp[j] = float('inf')
        else:
            min_mana = float('inf')  # initialize minimum mana to infinity
            for k in range(j):
                if k not in dp:  # check if we have already calculated the minimum mana for this monster
                    break
                min_mana = min(min_mana, dp.get(k, 0) + 1)  # update minimum mana
            dp[j] = min_mana  # store minimum mana required to kill current monster

    return sum(1 for j in dp if dp[j] < float('inf'))  # calculate the total mana needed

n = int(input())
ki = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]

print(min_mana_required(n, ki, h))
