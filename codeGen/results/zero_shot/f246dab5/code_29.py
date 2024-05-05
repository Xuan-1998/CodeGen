import sys

n = int(sys.stdin.readline())
total_cost = 0
used_tickets = {"day": False, "90min": False}

for _ in range(n):
    t = int(sys.stdin.readline())
    if not used_tickets["day"]:
        if t < 14 * 60:  # 14 hours in minutes
            total_cost += 50
            used_tickets["90min"] = True
        else:
            total_cost += 20
    elif not used_tickets["90min"]:
        total_cost += 50
        used_tickets["90min"] = True
    else:
        total_cost += 20

print(total_cost)
