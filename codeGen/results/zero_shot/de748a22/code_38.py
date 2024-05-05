n, q = map(int, input().split())
arr = list(input())

total_sum, sign_var_sum = preprocess(arr)

for _ in range(q):
    l, r = map(int, input().split())
    result = answer_query(total_sum, sign_var_sum, l, r)
    print(result)
