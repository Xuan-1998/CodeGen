n = int(input())
a = list(map(int, input().split()))
for i in range(2, n+1):
    y = simulate_program(a[i-1:i])
    print(y)
