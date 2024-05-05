def solve():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        if (u & 1) == (v & 1):  # Check if both are odd or both are even
            print("YES" if u <= v else "NO")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
