from collections import defaultdict

def can_form_polygon(knights):
    memo = defaultdict(bool)

    def dfs(k, p):
        if (k, p) in memo:
            return memo[(k, p)]

        if k % 3 == 0 and p == 1 or k % 3 != 0 and p == 0:
            if all((knights[i-1] + knights[i]) % 2 == 0 for i in range(1, k)):
                memo[(k, p)] = True
                return True
            else:
                memo[(k, p)] = False
                return False

        if k > 0 and all((knights[i-1] + knights[i]) % 2 == 0 for i in range(1, k)):
            if (k - 1, 0) not in memo or dfs(k - 1, 0):
                memo[(k, p)] = True
                return True
            else:
                memo[(k, p)] = False
                return False

        memo[(k, p)] = False
        return False

    return "YES" if dfs(len(knights), 1) else "NO"


# Example usage:
knights = list(map(int, input().split()))
print(can_form_polygon(knights))
