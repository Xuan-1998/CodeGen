def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a):
            return -1
        a_x = a[x]
        x += a_x
        y += a_x
        x -= a_x
        y += a_x

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(a))  # Run the program for each sequence
