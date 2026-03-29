def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp_table = [0] * (n + 1)
        dp_table[n] = 1
        for i in range(m - 1, -1, -1):
            new_dp_table = [0] * (n + 1)
            for j in range(n, -1, -1):
                new_dp_table[j] = (new_dp_table.get(j, 0) + dp_table.get((j + 1) % 10, 0)) % 1000000007
            dp_table = new_dp_table
        print(dp_table[1] % 1000000007)

if __name__ == "__main__":
    solve()
