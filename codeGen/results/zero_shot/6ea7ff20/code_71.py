def solve(n):
    p = [int(x) for x in input().split()]
    if can_split(p):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
