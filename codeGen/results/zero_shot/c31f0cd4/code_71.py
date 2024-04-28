n = int(input())
nums = list(map(int, input().split()))
dp = [[num] for num in nums]
dp.append([])
for i in range(n):
    new_dp = []
    for j in range(len(dp)):
        if len(dp[j]) <= i:
            continue
        for k in range(i+1):
            new_dp.append(sorted(list(set((set(dp[j][:-k]) & set([nums[i]])) | set([nums[i]])))) + dp[j][-k:])
dp = [item for sublist in dp for item in sublist]
print(' '.join(str(sum(num)) for num in sorted(set(tuple(sorted(num)) for num in dp))))
