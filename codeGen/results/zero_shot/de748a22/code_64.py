import sys

n, q = map(int, input().split())
signs = list(input())

cum_sum_signs = 0
running_sum_signs = [0]
for sign in signs:
    cum_sum_signs += 1 if sign == "+" else -1
    running_sum_signs.append(cum_sum_signs)

for _ in range(q):
    l, r = map(int, input().split())
    left_sum_signs = running_sum_signs[r] - running_sum_signs[l-1]
    right_sum_signs = 0
    for i in range(l-1, r+1):
        if signs[i] == "+":
            right_sum_signs += 1
        else:
            right_sum_signs -= 1
    
    max_positive = max(0, left_sum_signs // 2 + (left_sum_signs % 2) != 0)
    max_negative = -max_positive
    if left_sum_signs > 0 and right_sum_signs < 0:
        print(r-l+1-math.ceil(max_positive))
    elif left_sum_signs < 0 and right_sum_signs > 0:
        print(r-l+1-math.floor(-max_negative))
    else:
        print(min(left_sum_signs, -right_sum_signs) * 2)
