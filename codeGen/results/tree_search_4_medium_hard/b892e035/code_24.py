import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probs = []
        prev_nums = set()
        for _ in range(n):
            p, num1, num2 = map(float, sys.stdin.readline().split())
            if num1 not in prev_nums and num2 not in prev_nums:
                prev_nums.add(num1)
                prev_nums.add(num2)
            probs.append(p)
        total_prob = 1.0
        for i in range(1, n):
            curr_probs = []
            for p, _, _ in zip(probs, prev_nums, [num1, num2]):
                if num1 == prev_nums.pop():
                    curr_probs.append(p * total_prob)
                else:
                    curr_probs.append((1 - p) * total_prob)
            total_prob = sum(curr_probs) / len(curr_probs)
        print("{:.6f}".format(total_prob))

calculate_probability()
