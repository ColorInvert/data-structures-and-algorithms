class BinaryTree:
    """
    Basic binary tree structure. Can output a tree node manifest as an array through either
    pre-order, in-order, or post-order sorting.
    """

    def __init__(self):
        self.root = None
        self.output = []



    #? Pre order, in order, and post order are the same, except for when the root's
    #? value is noted down. Before, during or after.

    def pre_order(self, node=None):

        # establish tree root
        if node is None:
            node = self.root

        # add value of current node to array
        self.output.append(node.value)

        # Check if left exists, and if so, traverse down recursively
        if node.left is not None:
            self.pre_order(node.left)

        # Check if right exists, and if so, traverse down recursively
        if node.right is not None:
            self.pre_order(node.right)

        return self.output


    def in_order(self, node=None):

        # establish tree root
        if node is None:
            node = self.root

        # Check if left exists, and if so, traverse down recursively
        if node.left is not None:
            self.in_order(node.left)

        # add value of current node to array
        self.output.append(node.value)

        # Check if right exists, and if so, traverse down recursively
        if node.right is not None:
            self.in_order(node.right)

        return self.output

    def post_order(self, node=None):

        # establish tree root
        if node is None:
            node = self.root

        # Check if left exists, and if so, traverse down recursively
        if node.left is not None:
            self.post_order(node.left)

        # Check if right exists, and if so, traverse down recursively
        if node.right is not None:
            self.post_order(node.right)

        # add value of current node to array
        self.output.append(node.value)

        return self.output


class Node:

    # Each node can hold it's own value, and the location of the node to its left and right.
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

