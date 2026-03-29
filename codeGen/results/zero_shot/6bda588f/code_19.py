def min_F_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        min_F = float('inf')
        for i in range(n-1):
            max_x = min(a[i], s)
            min_y = max(0, a[i] - s)
            F = max_x * (a[i+1] - min_y) + min_y * a[i]
            min_F = min(min_F, F)
        print(min_F)

if __name__ == "__main__":
    min_F_value()
