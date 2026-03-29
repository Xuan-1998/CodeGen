def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(num_stable_tables(N, M))

if __name__ == "__main__":
    main()
