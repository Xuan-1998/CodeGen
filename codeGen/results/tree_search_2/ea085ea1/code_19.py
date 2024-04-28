from collections import defaultdict

def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = defaultdict(int)
    max_length = 0

    for i in range(N):
        for j in range(N):
            if str1[i] == str2[N-1-j]:
                k = N-1
                while k > i and k > j:
                    if str1[k-N+1:i+1] != str2[0:j+1]:
                        break
                    dp[(i, j, k)] += 1
                    max_length = max(max_length, dp[(i, j, k)])
                    k -= 1

    return max_length

print(max_common_substrings())
