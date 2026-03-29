def can_send_over_network(b):
    n = len(b)
    a = [0]  # Initialize a with a single element (empty segment)

    for i, x in enumerate(b):
        if a[-1] == 0:  # Left-insertion is allowed only when a is empty or the last segment has length 0
            a.append(x)  # Insert x at the end of a
        else:
            a.insert(1, x)  # Insert x between the two previous segments

    return "YES" if a == list(map(str, b)) else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    b = [int(x) for x in input().split()]
    print(can_send_over_network(b))
