import sys

# Read input from stdin
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

# Initialize maximum total joy to 0
max_total_joy = 0

# Iterate over all possible orders of feeding the hares
for order in range(1 << n):  # 2^n possible orders
    total_joy = 0
    prev_state = None  # previous state (hungry or full)
    for i in range(n):
        if ((order >> i) & 1):  # feed hare at position i
            if prev_state is None:  # first hare, set prev_state to hungry
                prev_state = 0
            elif prev_state == 0:  # previous hare was hungry, add joy value of b_i
                total_joy += b[i]
            else:  # previous hare was full, add joy value of c_i
                total_joy += c[i]
        prev_state = ((prev_state + 1) % 2)  # update previous state

    max_total_joy = max(max_total_joy, total_joy)

print(max_total_joy)
