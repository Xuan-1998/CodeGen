n = int(input())  # number of booking requests
bookings = []  # list of booking requests
for _ in range(n):
    group_size, money = map(int, input().split())
    bookings.append((group_size, money))

k = int(input())  # number of tables
max_capacity = int(input())  # maximum capacity of each table

bookings.sort(key=lambda x: x[1] / x[0])

total_money_earned = 0
table_assignments = []
for i, (group_size, money) in enumerate(bookings):
    while len(table_assignments) < group_size:
        if not table_assignments or len(table_assignments[-1]) + 1 <= max_capacity:
            table_assignments.append([i])
        else:
            break
    total_money_earned += money

accepted_requests = len(table_assignments)
print(accepted_requests, total_money_earned)

for i, table in enumerate(table_assignments):
    if table:
        print(i + 1, table[0])
