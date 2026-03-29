def can_obtain_sequence(b):
    n = len(b)
    a = [0]  # Initialize a with a single element

    cumulative_sum = 0
    for x in b:
        while cumulative_sum + (x + 1) > a[-1]:
            a.append(cumulative_sum + x)
        cumulative_sum += x

    return a == sorted(a)

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_obtain_sequence(b) else "NO")
