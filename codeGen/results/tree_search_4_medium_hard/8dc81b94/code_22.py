    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split()))
            if max(nums) > 10**6:
                print("NO")
            else:
                print(isPossibleToMakeEqualZero(nums))
        except EOFError:
            break
