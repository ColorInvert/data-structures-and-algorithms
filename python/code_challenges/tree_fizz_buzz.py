from data_structures.binary_tree import BinaryTree

# Import KaryTree from kary_tree for clone assembly
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):

    # Transform function for handling on fly cloning and modification of clones
    def transform(node):
        # Base case of no root
        if node is None:
            return None

        # Divisible by 3 and 5?
        if node.value % 3 == 0 and node.value % 5 == 0:
            clone_node = Node("FizzBuzz")
        # Divisible by 3 only?
        elif node.value % 3 == 0:
            clone_node = Node("Fizz")
        # Divisible by 5 only?
        elif node.value % 5 == 0:
            clone_node = Node("Buzz")
        # None of these, clone value, but as string
        else:
            clone_node = Node(str(node.value))

        # Get the children manifest of current node, and recursively call Transform on them
        # before appending the results to the children list of current node.
        for child in node.children:
            modified_child = transform(child)
            clone_node.children.append(modified_child)
        return clone_node

    # With all children modified, transform the root
    cloned_root = transform(tree.root)

    # form tree off of cloned root and modified children.
    return KaryTree(cloned_root)
