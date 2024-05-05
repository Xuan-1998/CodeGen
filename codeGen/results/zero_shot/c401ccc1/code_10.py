def check_path(q):
    for _ in range(q):
        u, v = map(int, input().split())
        if u ^ v != 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    q = int(input())
    check_path(q)
