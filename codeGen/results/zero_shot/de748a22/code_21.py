def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input()))
    pos, neg = 0, 0
    for sign in arr:
        if sign == 1:
            pos += 1
        else:
            neg += 1
    
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        pos_range, neg_range = sum(arr[i] for i in range(l, r+1)), 0
        for sign in arr[l:r+1]:
            if sign == 1:
                pos_range -= 1
            else:
                neg_range += 1
        
        queries.append((pos_range, neg_range))
    
    for query in queries:
        pos_range, neg_range = query
        print(min(pos_range + neg_range // 2, n - pos_range - (neg_range + 1) // 2))

if __name__ == '__main__':
    solve()
