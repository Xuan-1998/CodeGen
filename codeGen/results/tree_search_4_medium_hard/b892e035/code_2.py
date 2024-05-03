import math

dp_state = [(0, set())]
for i in range(n):
    for prev_i, prev_used in dp_state:
        p1, num1, num2 = input().split()
        p1, num1, num2 = float(p1), int(num1), int(num2)
        new_used = (prev_used | {num1, num2}) - {num1}
        if i == 0 or len(new_used) == len(prev_used):
            dp_state.append((i+1, new_used))

for _ in range(T):
    n = int(input())
    dp = [1.0]
    for i in range(n):
        p1, num1, num2 = input().split()
        p1, num1, num2 = float(p1), int(num1), int(num2)
        new_dp = []
        for prev_i, prev_used in dp:
            if len(prev_used) == i+1 and num1 not in prev_used and num2 not in prev_used:
                prob = 1.0
                for num in prev_used:
                    if num == num1:
                        prob *= (1 - p1)
                    elif num == num2:
                        prob *= p2
                new_dp.append((prev_i + 1, prob))
        dp = new_dp
    print(sum(p ** (i-1) for i, _ in enumerate(dp)))
