def calculate_probability(n, P1, A1, B1):
    if n == 0:
        return 1

    probability = (P1 * (1 - P1)) / n
    remaining_tickets = n - 1

    # Calculate the probability of correct numbering given the current state and the new ticket's numbers and probabilities.
    probability *= calculate_probability(remaining_tickets, (1 - P1) * A1, B1 - A1, (1 - P1))

    return probability


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        P, A, B = map(int, input().split())

        print(calculate_probability(n, P, A, B))


if __name__ == "__main__":
    main()
