def find_x(A, B):
    if A == 0 or B == 0:
        return 0

    memo = {}

    def helper(x):
        if (x, A) in memo:
            return memo[(x, A)]
        
        y = (A - x) ^ (B - x)
        if y > x:
            y = (y + x) // 2
        
        res = min([x, helper(min(A - 1, B))])
        memo[(x, A)] = res
        return res

    return helper((A + B) // 2)

def main():
    A = int(input())
    B = int(input())

    X = find_x(A, B)
    
    if X == 0:
        print(-1)
    else:
        Y = (A - X) ^ (B - X)
        print(X, Y)

if __name__ == "__main__":
    main()
