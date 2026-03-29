def preprocess_array(signs):
    n = len(signs)
    total_sum = 0
    sign_var_sum = 0
    for i in range(n):
        if signs[i] == "+":
            total_sum += 1
            sign_var_sum += 1
        else:
            total_sum -= 1
            sign_var_sum -= 1
    return total_sum, sign_var_sum

def process_query(total_sum, sign_var_sum, l, r):
    query_sum = total_sum - sign_var_sum
    for i in range(l-1, r):
        if signs[i] == "+":
            query_sum -= 1
        else:
            query_sum += 1

    min_remove = abs(query_sum)
    return min_remove

n, q = map(int, input().split())
signs = list(input())

total_sum, sign_var_sum = preprocess_array(signs)

for _ in range(q):
    l, r = map(int, input().split())
    min_remove = process_query(total_sum, sign_var_sum, l, r)
    print(min_remove)
