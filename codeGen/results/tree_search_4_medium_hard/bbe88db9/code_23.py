import sys

def Transition(room, visited, crosses):
    if room < n+1:
        if visited and crosses % 2 == 0:  # ceiling has even number of crosses
            return (room + 1, False, 0)  # go to next room with no crosses
        else:
            return (p[room-1], True, crosses+1)  # use second portal with odd crosses
    elif room == n+1:
        return None  # reached destination

n = int(input())
p = [int(x) for x in input().split()]

dp = {}
for room in range(1, n+2):
    for visited in [False, True]:
        for crosses in range(3):  # 0, 1, and 2
            if (room, visited, crosses) not in dp:
                dp[(room, visited, crosses)] = float('inf')
                next_states = Transition(room, visited, crosses)
                if next_states is not None:
                    state_value = dp[next_states] + 1
                    dp[(room, visited, crosses)] = min(dp[(room, visited, crosses)], state_value)

print((dp.get((n+1, True, 2), float('inf')) - 1) % (10**9 + 7))
