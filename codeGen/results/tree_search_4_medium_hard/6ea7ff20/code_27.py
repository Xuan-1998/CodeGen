if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print('YES' if mergeable(p) else 'NO')
