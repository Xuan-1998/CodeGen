import sys

def max_earnable_tables(requests, k):
    n = len(requests)
    memo = {}

    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        earnable = 0
        for ci, ri in requests:
            if ri <= k and ci * ri <= j:
                accept_earn = dp(i-1, j-ci*ri)
                decline_earn = dp(i, j-ci*ri)
                earnable = max(accept_earn + ri, decline_earn)
                memo[(i, j)] = earnable
                break

        return earnable

    earnable = dp(k, sum(r[1] for r in requests))
    accepted_requests = 0
    total_money_earned = 0
    remaining_tables = k
    remaining_money = sum(r[1] for r in requests)

    while accepted_requests < n:
        for ci, ri in requests:
            if ri <= remaining_tables and ci * ri <= remaining_money:
                total_money_earned += ri
                accepted_requests += 1
                remaining_tables -= ci
                remaining_money -= ci * ri
                break

    print(accepted_requests)
    print(total_money_earned)

    for i, (ci, _) in enumerate(requests):
        if i < accepted_requests:
            print(i+1, remaining_tables+1)

max_earnable_tables([ [2, 10], [3, 15], [4, 20] ], 5)
