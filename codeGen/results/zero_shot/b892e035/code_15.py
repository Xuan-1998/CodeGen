T = int(input())  # number of test cases

for _ in range(T):
    n = int(input())  # number of tickets
    A = []  # list of possible numbers on each ticket
    P = []  # list of probabilities for each number
    
    for i in range(n):
        A_i, B_i, P_i = map(float, input().split())
        A.append(A_i)
        B.append(B_i)
        P.append(P_i)
    
    p = calculate_probability(n)  # calculate the probability
    print(f"{p:.6f}")  # print the result with rounding to 6 decimal places
