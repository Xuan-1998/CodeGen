if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        a = list(map(int, input().split()))
        print(max_score(a))
