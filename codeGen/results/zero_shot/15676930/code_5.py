n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Calculate the maximum total joy
max_total_joy = 0

for i in range(n):
    if i == 0:  # first hare
        max_total_joy += c[i]
    elif i == n - 1:  # last hare
        max_total_joy += a[i]
    else:
        max_total_joy += b[i]

print(max_total_joy)
