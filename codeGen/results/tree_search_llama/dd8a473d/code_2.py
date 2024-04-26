class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(node):
    if node is None:
        return 'null'
    else:
        result = str(node.value)
        if node.next is not None:
            result += ' -> ' + stringify(node.next)
        return result

# test the function
node1 = Node(5)
node2 = Node(6)
node3 = Node(7)

node1.next = node2
node2.next = node3

print(stringify(node1))
