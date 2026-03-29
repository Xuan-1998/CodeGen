import sys

dp = {0: 20}  # base case: one trip, always 20 BYT
total_fare = 0
n = int(input())

for t in range(n):
    i = t % 1440  # convert to minutes of the day
    if i < 90:
        total_fare += dp.get(i-1, 20) + 20
    elif i <= 1260:  # one day (14 hours)
        total_fare += min(dp.get(i-2, 120), dp.get(i-3, 120)) + 50
    else:
        total_fare += 120

print(total_fare)
