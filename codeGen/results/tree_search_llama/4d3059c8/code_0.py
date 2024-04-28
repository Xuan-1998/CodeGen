if __name__ == "__main__":
    tree = AVLTree()
    nums = [int(x) for x in sys.stdin.readline().split()]
    tree.insert(nums[0])
    pivot_idx = -1
    left_sum = 0
    right_sum = sum(nums)

    for i, num in enumerate(nums):
        if left_sum == right_sum:
            pivot_idx = i
            break
        elif left_sum < right_sum:
            left_sum += num
        else:
            right_sum -= num

    print(pivot_idx)
