def solve(t):
    MOD = 10**9 + 7
    result = []
    for _ in range(t):
        n, m = map(int, input().split())
        num_str = str(n)
        for _ in range(m):
            new_num_str = ''
            for d in num_str:
                new_d = (int(d) + 1) % 10
                new_num_str += str(new_d)
            num_str = new_num_str
        result.append(len(str(int(num_str))) % MOD)
    print(*result, sep='\n')

if __name__ == '__main__':
    t = int(input())
    solve(t)
