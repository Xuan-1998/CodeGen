def max_xor_sum(A, X):
    memo = {}
    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return [0, 0]  # base case
        result = [0, 0]
        for j in range(0, i):
            temp1 = dp(j)[1] + (A[j+1]-X)*XOR(A[j+2])
            temp2 = dp(j)[0] + A[j+1]*XOR(A[j+2])
            result[0] = max(result[0], temp1)
            result[1] = max(result[1], temp2)
        memo[i] = result
        return result

    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        print(max(dp(N-1)[0], dp(N-1)[1]))
