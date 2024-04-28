if __name__ == "__main__":
    nums = [list(map(int, input().split())) for _ in range(10)]
    for num in nums:
        print(longest_subarray(num))
