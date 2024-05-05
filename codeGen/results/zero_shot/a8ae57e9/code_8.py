n = int(input())
booking_requests = []
for _ in range(n):
    group_size, total_amount = map(int, input().split())
    booking_requests.append((group_size, total_amount))
k = int(input())
max_capacity = int(input())

booking_requests.sort(key=lambda x: x[1], reverse=True)
accepted_requests = 0
earned_money = 0

for group_size, total_amount in booking_requests:
    if k > 0 and group_size <= max_capacity:
        accepted_requests += 1
        earned_money += total_amount
        k -= (max_capacity - 1) // group_size

print(accepted_requests, earned_money)
for i, request in enumerate(booking_requests):
    if i < accepted_requests:
        group_size, total_amount = request
        table_number = (max_capacity - 1) // group_size + 1
        print(i+1, table_number)
