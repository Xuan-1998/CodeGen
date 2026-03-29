from typing import List

def solve() -> None:
    n = int(input())  # number of booking requests
    requests: List[tuple] = []
    for _ in range(n):
        group_size, total_amount = map(int, input().split())
        requests.append((group_size, total_amount))
    
    requests.sort(key=lambda x: x[1], reverse=True)
    
    accepted_requests = 0
    total_money_earned = 0
    
    tables = [int(input())] * k  # maximum capacity of each table
    
    for group_size, total_amount in requests:
        if all(table >= group_size for table in tables):
            accepted_requests += 1
            total_money_earned += total_amount
            # update the remaining capacity of the chosen table
            tables[tables.index(max(tables))] -= group_size
        else:
            break
    
    print(accepted_requests)
    print(total_money_earned)
    
    for i, (group_size, _) in enumerate(requests):
        if i < accepted_requests:
            print(f"{i+1} {tables.index(max(tables)) + 1}")
