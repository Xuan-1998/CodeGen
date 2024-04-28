n = int(input())
nums = list(map(int, input().split()))
all_sums = set()
def dfs(index, path_sum):
    if index == n:
        all_sums.add(path_sum)
        return
    for i in range(1, 101):
        if i > nums[index]:
            break
        if i not in nums[:index]:
            dfs(index + 1, path_sum + i)
print(' '.join(map(str, sorted(all_sums))))
