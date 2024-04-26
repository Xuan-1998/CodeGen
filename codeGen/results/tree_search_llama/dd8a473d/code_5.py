class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def stringify(head):
    if head is None:
        return "null"

    stack = []
    node = head
    while node:
        stack.append(str(node.val))
        node = node.next

    result = "->".join(reversed(stack)) + " null"
    return result

# Example usage:
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third

print(stringify(head))  # Output: "3->2->1 null"
