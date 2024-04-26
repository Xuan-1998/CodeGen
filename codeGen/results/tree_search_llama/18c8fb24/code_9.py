def solution():
    T = int(input())
    for _ in range(T):
        N, x, k = map(int, input().split())
        if forward_trajectory(x, N, k) >= x:
            print("YES")
        else:
            print("NO")

def forward_trajectory(x, N, k):
    r = k / (N+2)
    total_distance = 0
    for i in range(1, x//k + 1):  # ceiling division
        total_distance += r ** i * k
    return total_distance

solution()
