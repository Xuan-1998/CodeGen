import sys

def solve():
    n = int(input())
    dp = {(0, 0): 0}  # base case: no more minutes left until ticket expires

    for _ in range(n):
        t = int(input())
        minutes_left_until_ticket_expires = max(0, 90 - (t % 90))
        total_cost_so_far = dp.get((minutes_left_until_ticket_expires, 0), float('inf'))

        if minutes_left_until_ticket_expires == 0:
            minutes_left_until_ticket_expires = 1440 - (t % 1440)
            total_cost_so_far += 120

        for ticket_minutes in [1, 90, 1440]:
            new_minutes_left_until_ticket_expires = max(0, ticket_minutes - (t % ticket_minutes))
            new_total_cost_so_far = total_cost_so_far + (ticket_minutes // 60) * 20
            dp[(new_minutes_left_until_ticket_expires, new_total_cost_so_far)] = min(dp.get((new_minutes_left_until_ticket_expires, new_total_cost_so_far), float('inf')), total_cost_so_far)

        print(total_cost_so_far)

solve()
