def solve():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read initial number and operations
        len_n = len(str(n))  # initialize length of initial number
        for _ in range(m):
            new_n = int(''.join(str(d+1) for d in str(n)))  # apply operation
            len_n = len(str(new_n))  # update length after applying an operation
        print(len_n % (10**9 + 7))  # print the final result

if __name__ == "__main__":
    solve()
