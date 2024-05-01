import sys

def collapse_sequence(seq):
    n = len(seq)
    collapsed_seq = []

    for i in range(n):
        if i > 0 and seq[i] == seq[i-1]:
            continue
        if i < n - 1 and seq[i] == seq[i+1]:
            continue
        collapsed_seq.append(seq[i])

    return collapsed_seq

def count_points(collapsed_seq):
    unique_points = set()
    for point in collapsed_seq:
        unique_points.add(point)
    return len(unique_points)

n = int(sys.stdin.readline())
seq = [int(x) for x in sys.stdin.readline().split()]

collapsed_seq = collapse_sequence(seq)
points = count_points(collapsed_seq)

print(points)
