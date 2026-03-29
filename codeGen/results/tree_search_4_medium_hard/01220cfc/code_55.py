def can_reach(arr):
    memo = {0: True}  # base case: starting from index 0 is possible

    for i in range(len(arr)):
        if i not in memo:
            continue
        jump_length = arr[i]
        for j in range(i - jump_length, -1, -1):
            if j not in memo or not memo[j]:
                break
        else:  # reached the start of the array without breaking
            memo[i + 1] = True

    return memo.get(len(arr) - 1, False)

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(can_reach(arr))
