def maxJoy(hungryHares, oneFull, bothFull):
    dp = {(i, 0): [0, float('inf')] for i in range(len(hungryHares))}
    
    for i in range(1, len(hungryHares)):
        prevHungry = (i-1, 0) if i > 0 else None
        prevOneFull = (i-1, 1) if i > 0 and oneFull[i-1] > bothFull[i-1] else None
        prevBothFull = (i-1, 2) if i > 0 and oneFull[i-1] == bothFull[i-1] else None
        
        for j in range(3):
            if j == 0: # hungry hare
                if prevHungry:
                    dp[(i, j)] = [dp[prevHungry][0] + hungryHares[i], dp[prevHungry][1]]
                else:
                    dp[(i, j)] = [hungryHares[i], float('inf')]
            elif j == 1: # one full
                if prevOneFull and dp[prevOneFull][1] > bothFull[i-1]:
                    dp[(i, j)] = [dp[prevOneFull][0] + oneFull[i], dp[prevOneFull][1]]
                else:
                    dp[(i, j)] = [oneFull[i], float('inf')]
            elif j == 2: # both full
                if prevBothFull and dp[prevBothFull][1] > bothFull[i-1]:
                    dp[(i, j)] = [dp[prevBothFull][0] + bothFull[i], dp[prevBothFull][1]]
                else:
                    dp[(i, j)] = [bothFull[i], float('inf')]
    
    return max((dp[(n-1, i)][0] for i in range(3)))

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(maxJoy(a, b, c))
