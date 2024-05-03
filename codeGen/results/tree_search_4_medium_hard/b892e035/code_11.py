import sys

def calculate_probability():
    T = int(input())  # number of test cases
    memo = {}

    for _ in range(T):
        n = int(input())  # number of tickets
        probabilities = []
        for _ in range(n):
            P, A, B = map(int, input().split())
            probabilities.append((P, A, B))

        current_state = 0  # initial state (all incorrect numbers)
        probability = 1.0  # initial probability

        for P, A, B in probabilities:
            if memo.get(current_state, {}).get(A, {}):
                # if we've seen this number before, skip it
                probability *= memo[current_state][A]
            else:
                # calculate the new probability based on the current ticket's options
                new_probability = (P / 100) * (1 - probability)
                memo.setdefault(current_state, {})[A] = new_probability
                memo.setdefault(current_state, {})[B] = 1 - new_probability

            current_state |= 2 ** A if P > B else 2 ** B
            probability *= (P / 100)

        print("{:.6f}".format(probability))  # print the final probability with 6 decimal places

if __name__ == "__main__":
    calculate_probability()
