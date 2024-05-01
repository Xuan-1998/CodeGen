def find_max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp1 = [0] * (N + 1)
    dp2 = [0] * (N + 1)

    common_substr_found1 = [False] * (N + 1)
    common_substr_found2 = [False] * (N + 1)

    for i in range(N):
        for j in range(i, N):
            substr1 = str1[i:j+1]
            if substr1 in str2:
                if not common_substr_found1[i]:
                    dp1[j+1] = max(dp1[j], dp1[i-1]) + 1
                    common_substr_found1[i] = True

    for i in range(N):
        for j in range(i, N):
            substr2 = str2[i:j+1]
            if substr2 in str1:
                if not common_substr_found2[i]:
                    dp2[j+1] = max(dp2[j], dp2[i-1]) + 1
                    common_substr_found2[i] = True

    return min(dp1[-1], dp2[-1])

print(find_max_common_substrings())
