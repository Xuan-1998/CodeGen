n, q = map(int, input().split())
signs = list(input())

total_sum = sum(signs)
sign_variable_sum = total_sum % 2

for _ in range(q):
    l, r = map(int, input().split())
    
    left_signs = signs[:l]
    right_signs = signs[r:]
    middle_signs = signs[l:r+1]
    
    middle_sum = sum(middle_signs)
    sign_variable_middle_sum = middle_sum % 2
    
    if sign_variable_middle_sum == 0:
        print(0)  # No elements need to be removed
    else:
        remaining_sum = (total_sum - middle_sum) % 2
        if remaining_sum == 0:
            print(len(middle_signs))  # Remove all middle elements
        else:
            print(min(left_signs.count(sign_variable_middle_sum), right_signs.count(sign_variable_middle_sum)))  # Remove the minimum number of elements from either side
