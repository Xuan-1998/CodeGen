def find_xor_pair(A, B):
    memo = { (0, 0): 0 }

    for X in range(1, A//2 + 1):
        Y = A - X
        state = (A, B ^ X)
        if state not in memo:
            memo[state] = min(X, find_xor_pair(Y, B ^ X))
        else:
            result = memo[state]
            break
    else:
        result = -1

    return str(result) + " " + str(A - result)

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    print(find_xor_pair(A, B))
