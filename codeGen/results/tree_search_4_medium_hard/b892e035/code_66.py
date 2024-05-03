from math import comb

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = {(0, 0, 0): 1}  # Base case: probability of correct numbering with no tickets and no numbers seen yet
        for i in range(1, n+1):
            p1, num1, num2 = map(int, input().split())
            new_dp = {}
            for (j, count1, count2) in list(dp.keys()):
                if num1 != num2:  # If the current ticket has a distinct number from previously seen numbers
                    new_dp[(i, max(count1, 0), max(count2, 0))] = dp[(j, count1, count2)] * p1 * (1 - comb(min(i-1, count1+count2), count1) / comb(i-1, count1))
                    new_dp[(i, max(0, j-count1), max(count2, 0))] = dp[(j, count1, count2)] * (1 - p1) * (1 - comb(min(i-1, count2+count1), count2) / comb(i-1, count2))
                    new_dp[(i, max(count1, 0), max(0, j-count2))] = dp[(j, count1, count2)] * p1 * (1 - comb(min(i-1, count1+count2), count2) / comb(i-1, count2))
                else:
                    new_dp[(i, min(count1+1, 16), max(0, j-count1))] = dp[(j, count1, count2)] * (1 - p1) * (1 - comb(min(i-1, count1+count2), count1) / comb(i-1, count1))
                    new_dp[(i, max(count1, 0), min(count2+1, 16))] = dp[(j, count1, count2)] * p1 * (1 - comb(min(i-1, count1+count2), count2) / comb(i-1, count2))
            dp.update(new_dp)
        print(sum(dp.values()))

if __name__ == "__main__":
    solve()
