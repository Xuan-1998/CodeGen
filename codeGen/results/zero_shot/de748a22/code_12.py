def solve():
    n = int(input())
    arr = list(map(int, input()))
    cum_sum = preprocess_array(arr)
    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(answer_query(cum_sum, l, r))

if __name__ == "__main__":
    solve()
