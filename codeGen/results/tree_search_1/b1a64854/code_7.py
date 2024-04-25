def find_min_sum(N, M):
    # If N equals M, the minimum sum is N (diagonal filled with 1's)
    # Otherwise, it is impossible, so the minimum sum is 0
    return N if N == M else 0

def main():
    T = int(input())  # Read number of test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Read N and M for each test case
        result = find_min_sum(N, M)
        print(result)

if __name__ == "__main__":
    main()
