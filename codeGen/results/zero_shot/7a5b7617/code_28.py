def count_steady_tables():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        count = 0
        for last_row_sum in range(M, -1, -1):
            row_sums = [0] * (N-1)
            for i in range(N-1):
                if sum(row_sums) + last_row_sum > M:
                    break
                row_sums[i] += 1
                while sum(row_sums) < last_row_sum:
                    row_sums[i] += 1
            else:
                count = (count + 1) % 1000000000
        print(count)

if __name__ == "__main__":
    count_steady_tables()
