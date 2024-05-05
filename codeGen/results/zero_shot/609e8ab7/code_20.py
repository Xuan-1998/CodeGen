import sys

def adjust_tree_values():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        p = [0] + list(map(int, sys.stdin.readline().split()))
        l, r = [], []
        for i in range(n):
            li, ri = map(int, sys.stdin.readline().split())
            l.append((li, 1))  # (range_start, operation_type: 1 for adjustment)
            r.append((ri, -1))  # (range_end, operation_type: -1 for "un-adjustment")
        l.sort()
        r.sort()

        min_ops = 0
        curr_range_start = float('inf')
        prev_op_type = None

        for i in range(len(l) + len(r)):
            if i < len(l):
                li, op_type = l[i]
            else:
                ri, op_type = r[-1 - i]

            # Adjust/Un-adjust the current node
            while curr_range_start <= li and (prev_op_type == 1 or prev_op_type == -1):
                if op_type == 1:  # Adjustment
                    min_ops += 1
                else:  # "Un-adjustment"
                    min_ops -= 1
                curr_range_start = ri + 1

            prev_op_type = op_type

        print(min_ops)

if __name__ == "__main__":
    adjust_tree_values()
