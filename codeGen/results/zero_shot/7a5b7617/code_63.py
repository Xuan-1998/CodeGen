def solve():
    t = int(input())  # read T test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read N and M
        total_sum = sum(range(m + 1))  # calculate the maximum possible sum
        result = 0
        for i in range(1, n):
            if (total_sum - (m * i)) < 0:  # check if the condition is satisfied
                break
            else:
                result += 1
        print(result % 1000000000)  # output the result

if __name__ == "__main__":
    solve()
