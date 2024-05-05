n = int(input())
sequence = list(map(int, input().split()))

for i in range(1, n):
    result = simulate_program(n, [0] + sequence)
    print(result if result != -1 else -1)
