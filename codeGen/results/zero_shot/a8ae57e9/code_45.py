accepted_requests = []
tables_assigned = []

requests.sort(key=lambda x: x[1], reverse=True)

for pi, ri in requests:
    for j in range(k):
        if len([i for i, (pi_, _) in enumerate(zip(accepted_requests, request_amounts))
                 if pi_ > 0 and i % k == j]) < capacity:
            accepted_requests.append(pi)
            tables_assigned.append((pi, j))
            break

total_earnings = sum(pi * ri for pi, ri in zip(accepted_requests, request_amounts))

print(f"Accepted requests: {len(accepted_requests)}")
print(f"Total earnings: {total_earnings}")
for i, (pi, j) in enumerate(tables_assigned):
    print(f"Request {i+1}: Table {j+1}")
