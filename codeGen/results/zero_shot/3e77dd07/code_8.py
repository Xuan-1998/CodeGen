class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def string_to_tree(s):
    if not s:
        return None
    node = Node(s[0])
    if len(s) == 1:
        return node
    mid = len(s) // 2
    node.left = string_to_tree(s[:mid])
    node.right = string_to_tree(s[mid:])
    return node

def is_scrambled(s1, s2):
    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)
    if not is_same_tree(t1, t2):
        return False
    return True

def is_same_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.char != t2.char:
        return False
    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)

def main():
    s1 = input()
    s2 = input()
    print(is_scrambled(s1, s2))

if __name__ == "__main__":
    main()
