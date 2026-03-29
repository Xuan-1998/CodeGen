def find_good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            subsequence = [a[i], a[j]]
            
            is_good = True
            for k in range(len(subsequence)):
                if subsequence[k] % (k+1) != 0:
                    is_good = False
                    break
            
            if is_good:
                count += 1

    print(count % MOD)
