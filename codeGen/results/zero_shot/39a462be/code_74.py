code
def main():
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    fill_dp_table(A, B)

    max_similarity = calculate_similarity_score(A, B)

    print(max_similarity)

if __name__ == "__main__":
    main()
