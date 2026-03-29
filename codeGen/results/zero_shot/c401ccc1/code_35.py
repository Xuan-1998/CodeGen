for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if has_path(u, v):
        print("YES")
    else:
        print("NO")
