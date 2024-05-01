def find_max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp1 = [0] * (N + 1)
    dp2 = [0] * (N + 1)

    for i in range(N):
        if str1[i] == str2[0]:
            dp1[i + 1] += 1
            dp2[1] += 1
        else:
            dp1[i + 1] = dp2[1] = 0

    for i in range(1, N):
        if str1[i] == str2[i]:
            dp1[i + 1] = dp1[i - 1] + 1
            dp2[i + 1] = dp2[i - 1] + 1
        else:
            dp1[i + 1] = max(0, dp1[i])
            dp2[i + 1] = max(0, dp2[i])

    count = 0
    for i in range(N):
        if dp1[i] > 0 and dp2[i] > 0:
            count += min(dp1[i], dp2[i])
    print(count)

if __name__ == "__main__":
    find_max_common_substrings()
