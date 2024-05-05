k = int(sys.stdin.readline())
tables = [0] * k

accepted_requests = 0
total_earned = 0
for pi_per_person, ci, pi in requests:
    for i in range(k):
        if tables[i] + ci <= k:  # table has enough capacity
            tables[i] += ci
            accepted_requests += 1
            total_earned += pi
            break

print(accepted_requests, total_earned)

# Print the accepted requests and tables assignments (not implemented here)
