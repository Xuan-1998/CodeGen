accepted_requests = []
total_earned = 0
table_usage = [0] * k  # keep track of used tables

for csi, pi in requests:
    # check if there's a table with enough capacity for this group
    for i, usage in enumerate(table_usage):
        if usage + csi <= k:  # table has enough capacity
            table_usage[i] += csi
            accepted_requests.append((csi, pi))
            total_earned += pi
            break

print(len(accepted_requests), total_earned)  # output the number of accepted requests and total earned

# print the tables to seat each group (if requested)
for i, request in enumerate(accepted_requests):
    csi, pi = request
    for j, usage in enumerate(table_usage):
        if usage == csi:
            print(i + 1, j + 1)  # output the request number and table number
