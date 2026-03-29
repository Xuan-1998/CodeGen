def can_send_over_network(b):
    n = len(b)
    for i in range(1 << n):  # iterate over all possible combinations of segments
        a = [0] * (n + 1)  # initialize the sequence a with zeros
        j = 0
        for k in range(n):
            if ((i >> k) & 1):  # if the k-th bit is set, add the length of the segment to a
                a[j + 1] = b[k]
                j += 1
        if all(a[i] == b[i] or (a[i - 1] and a[i] and a[i + 1]) for i in range(1, n)):
            return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
