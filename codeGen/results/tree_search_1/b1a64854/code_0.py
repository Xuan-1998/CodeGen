def min_sum_binary_matrix(N, M):
    return max(N, M)

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = min_sum_binary_matrix(N, M)
        print(result)

if __name__ == "__main__":
    main()
