t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # size of sequence b
    b = list(map(int, input().split()))  # sequence b itself

    a_segments = []  # keep track of current segment in a and its length
    for bi in b:
        found = False
        for ai in range(1, bi + 1):
            if len(a_segments) >= ai:
                new_segment = tuple((a_segments[-ai] - 1, bi))
                a_segments.extend(new_segment)
                found = True
                break
        if not found:
            print("NO")
            break
    else:
        print("YES")
