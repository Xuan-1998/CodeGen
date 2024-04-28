while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        ones = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                ones += 1
            else:
                ans = max(ans, ones)
                ones = 0
        ans = max(ans, ones)
        print(ans)
    except:
        break
