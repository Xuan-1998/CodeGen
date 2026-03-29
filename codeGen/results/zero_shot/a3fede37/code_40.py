def max_path_sum(arr):
    def dfs(index, current_sum):
        if index >= len(arr) or arr[index][0] == -1:
            return current_sum
        left_sum = dfs(2*index+1, current_sum+arr[index][0])
        right_sum = dfs(2*index+2, current_sum+arr[index][0])
        return max(left_sum, right_sum)

    max_sum = 0
    for i in range(len(arr)//2):
        max_sum = max(max_sum, dfs(i, arr[i][0]))
    return max_sum

# Read the binary tree from standard input
n = int(input())
arr = []
for _ in range(n):
    value, left_child_index, right_child_index = map(int, input().split())
    arr.append([value, left_child_index, right_child_index])

print(max_path_sum(arr))
