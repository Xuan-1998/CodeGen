if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    max_score = max_similarity_score(a, b)
    print(max_score)
