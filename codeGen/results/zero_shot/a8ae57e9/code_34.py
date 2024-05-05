import sys

n, k = map(int, input().split())
requests = []
for _ in range(n):
    size, money = map(int, input().split())
    requests.append((size, money))

requests.sort(key=lambda x: x[1], reverse=True)

total_money = 0
accepted_requests = []
table_seats = [k] * k

for size, money in requests:
    for i, seat in enumerate(table_seats):
        if seat >= size:
            table_seats[i] -= size
            total_money += money
            accepted_requests.append((size, money, i))
            break

print(len(accepted_requests), total_money)
for request in accepted_requests:
    print(*request)
