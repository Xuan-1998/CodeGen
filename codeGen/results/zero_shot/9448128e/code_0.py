dp[i][last] = number of valid sequences ending with 'last' from the first i sets

for i from 1 to N:
    for each element e in set A_i:
        if i == 1:
            dp[i][e] = 1
        else:
            for each element prev in set A_{i-1}:
                if prev != e:
                    dp[i][e] += dp[i-1][prev]
                    dp[i][e] %= MODULO

answer = sum(dp[N][e] for each element e in set A_N) % MODULO
