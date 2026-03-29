code block:
n, q = map(int, input().split())
array = list(input())
prefix_sum, suffix_sum = preprocess(array)
for _ in range(q):
    l, r = map(int, input().split())
    result = handle_query(prefix_sum, suffix_sum, l, r)
    print(result)
