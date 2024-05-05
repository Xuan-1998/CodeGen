def simulate_program(a_sequence):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > len(a_sequence):
            return -1
        a_val = a_sequence[x-1]
        x += a_val
        y += a_val
        x -= a_val
    return y

n = int(input())
a_sequence = list(map(int, input().split()))
for i in range(n-1):
    print(simulate_program(a_sequence))
