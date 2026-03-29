import math

def expected_carries(N):
    total_pairs = math.comb(10**N, 2)  # calculate the total number of pairs
    total_carries = 0
    
    for i in range(N):  # loop through each digit position
        carries_in_digit_position = 0
        
        # count the number of carries for this digit position
        for a in range(10):
            for b in range(10):
                if (a < 5 and b >= 5) or (a >= 5 and b < 5):
                    carries_in_digit_position += 1
        
        total_carries += carries_in_digit_position
    
    expected_value = total_carries / total_pairs
    return expected_value

T = int(input())  # read the number of test cases

for _ in range(T):
    N = int(input())  # read the maximum number of digits
    print(expected_carries(N))  # calculate and print the expected value
