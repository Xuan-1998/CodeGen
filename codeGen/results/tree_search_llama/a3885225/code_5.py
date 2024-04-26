def can_transform_to_palindrome(input_string):
    # Count the number of characters to flip
    flips = 0
    for i in range(len(input_string) // 2):
        if input_string[i] != input_string[-i - 1]:
            flips += 1

    return flips % 2 == 0

def main():
    while True:
        try:
            N = int(input())
            S = input().strip()
            if can_transform_to_palindrome(S):
                print("YES")
            else:
                print("NO")
        except EOFError:
            break

if __name__ == "__main__":
    main()

