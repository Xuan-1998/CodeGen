import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for a_x in sequence[1:]:
    result = simulate_program(sequence)
    print(result)
