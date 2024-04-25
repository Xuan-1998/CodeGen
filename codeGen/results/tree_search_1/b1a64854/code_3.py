def min_sum(N, M):
    return min(N, M)

def main():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        print(min_sum(N, M))

if __name__ == "__main__":
    main()
