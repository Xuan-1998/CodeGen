def count_matrices(N):
    dp = [0] * (N + 1)
    
    for i in range(3, N + 1):
        if i % 2 == 0:  # only odd numbers can be traces of matrices
            continue
        
        for a in range(i // 2 + 1):  # try all possible values for a (top-left entry)
            d = i - a  # calculate the value of d based on i and a
            if (a * d) % ((i - a) * ((i - a) + 1)) / 2:  # check if ad - bc is positive
                dp[i] += 1
    
    return dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
