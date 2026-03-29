import sys

def simulate_sequence(a):
    x, y = 1, 0
    max_y = -1

    for a_i in a:
        x += a_i
        y += a_i
        x -= a_i
        y += a_i

        if x <= 0 or x > len(a):
            break

        max_y = max(max_y, y)

    return max_y

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]

for i, a_i in enumerate(a):
    print(simulate_sequence([x for x in a[:i+1]]))
