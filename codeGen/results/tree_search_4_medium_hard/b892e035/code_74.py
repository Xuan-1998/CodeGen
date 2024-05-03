import sys

def prob_ticket(i, count1, count2):
    if i == 0:  # first ticket, no tickets yet
        return 1.0
    elif i == n:  # last ticket, we're done
        return 1.0
    else:
        prev_state = dp.get((i-1, (count1-1 if P_i[0] else count1, count2-1 if P_i[1] else count2)))
        if prev_state is None:  # memoization
            prev_state = prob_ticket(i-1, max(0, count1-1), max(0, count2-1))
            dp[(i-1, (count1-1 if P_i[0] else count1, count2-1 if P_i[1] else count2))] = prev_state
        return prev_state * P_i  # update state and probability

n = int(input())  # number of tickets
P = [list(map(float, input().split())) for _ in range(n)]  # probabilities of each ticket
dp = {(0, (0, 0)): 1.0}  # initialize memoization dictionary

prob = 0
for i in range(n):
    prob += prob_ticket(i+1, *dp.get((i, (sum(1 for j in P[:i] if j[0] == 1), sum(1 for j in P[:i] if j[1] == 2)))))
print(round(prob, 6))  # output the final probability
