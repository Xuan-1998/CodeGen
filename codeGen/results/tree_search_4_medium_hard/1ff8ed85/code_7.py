def can_obtain_sequence():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        memo = {(0, 0): True}
        prev_val = 0
        for length in range(1, n+1):
            for value in range(prev_val+1, min(length+1, max(b)+1)):
                if (length-1, value) not in memo or not b[length-1]:
                    memo[(length, value)] = False
                else:
                    memo[(length, value)] = True
                prev_val = value
            if not any((n, length) in memo for length in range(1, n+1)):
                print("NO")
                break
        else:
            print("YES")

can_obtain_sequence()
