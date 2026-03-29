import sys

def read_input():
    n = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))
    c_values = list(map(int, input().split()))
    return n, a_values, b_values, c_values

def max_total_joy(n, a_values, b_values, c_values):
    # Initialize maximum total joy and the order of feeding hares
    max_joy = 0
    feeding_order = []

    # Calculate the total joy for each possible feeding order
    for i in range(2**n):
        total_joy = 0
        last_hare_full = False
        for j in range(n):
            if ((i >> j) & 1):  # If hare j is fed
                if not last_hare_full:
                    total_joy += a_values[j]
                else:
                    total_joy += b_values[j]
            else:  # If hare j is not fed
                if last_hare_full:
                    total_joy += c_values[j]
                last_hare_full = ((i >> (j-1)) & 1) or ((i >> j) & 1)

        # Update the maximum total joy and feeding order
        if total_joy > max_joy:
            max_joy = total_joy
            feeding_order = list(range(n))
            for j in range(n):
                if ((max_joy >> (j-1)) & 1) or ((max_joy >> j) & 1):
                    feeding_order.remove(j)
                    break

    return max_joy, feeding_order

def main():
    n, a_values, b_values, c_values = read_input()
    max_joy, feeding_order = max_total_joy(n, a_values, b_values, c_values)
    print(max_joy)

if __name__ == "__main__":
    main()
