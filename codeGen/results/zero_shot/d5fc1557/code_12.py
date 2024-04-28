while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        ones = 0
        max_ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                max_ones = max(max_ones, ones)
            else:
                ones = 0
        print(max_ones)
    except:
        break
