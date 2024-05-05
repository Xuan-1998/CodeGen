def solve():
    n, k, c = map(int, input().split())  # number of booking requests, tables, and max capacity per table
    t = [0] * (k + 1)  # total amount spent by groups at each table
    
    for _ in range(n):
        g, a = map(int, input().split())  # group size and total amount spent
        t[min(k, g)] += a  # update the total amount spent at each table

    accepted_requests = 0  # initialize count of accepted requests
    total_earned = 0  # initialize total amount earned
    
    for i in range(1, k + 1):
        if t[i] > 0:  # if there are groups seated at this table
            remaining_space = c  # initialize space left at the table
            accepted_groups_at_table_i = 0  # initialize count of accepted groups at this table
            
            for g in range(i, -1, -1):  # try to seat groups from largest to smallest
                if t[g] <= remaining_space:  # if group fits at this table
                    total_earned += t[g]  # add amount earned from these groups
                    accepted_requests += 1  # increment count of accepted requests
                    remaining_space -= t[g]  # update space left at the table
                    break
    print(accepted_requests, total_earned)  # output accepted requests and total amount earned

    m = min(n, sum([g for g in range(1, k + 1) if t[g]]))  # number of accepted requests
    for _ in range(m):
        i, j = map(int, input().split())  # table index and group index
        print(i, j)
