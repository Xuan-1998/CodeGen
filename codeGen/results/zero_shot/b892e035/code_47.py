import math

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probabilities = []
        numbers = []
        for _ in range(n):
            p1, num1, num2 = map(int, input().split())
            probabilities.append(p1)
            numbers.append(num1)
            numbers.append(num2)
        
        # Calculate the total probability of each number
        num_probs = [0] * 17
        for i in range(16):
            num_probs[i] = math.log(probabilities[i])
        for i in range(n):
            if numbers[i] < 16:
                num_probs[numbers[i]] += math.log(1-probabilities[i])

        # Calculate the final probability of correct numbering
        total_prob = 0
        for i in range(17):
            total_prob += math.exp(num_probs[i])
        print(total_prob)

if __name__ == "__main__":
    solve()
