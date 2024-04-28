def can_sum_divisible(nums, m):
    memo = {0: True}  # Base case: an empty subset has a sum of 0

    for num in nums:
        new_memo = dict(memo)
        for s in list(memo.keys()):
            new_memo[s + num] = new_memo.get(s + num, False) or memo.get(s, False)

        # Update the memo with the new sums and their corresponding indices
        memo.update(new_memo)

    return memo.get(sum(nums), False)  # Check if there's a subset sum divisible by m

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    print(1 if can_sum_divisible(nums, m) else 0)
