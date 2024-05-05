n = int(input())
a = list(map(int, input().split()))
def simulate_program(a):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > n:
            return y
        a_x = a[x-1]
        x += a_x
        y += a_x

result = [simulate_program(a) for _ in range(n-1)]
print(*result, sep='\n')
