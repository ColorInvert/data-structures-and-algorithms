from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A binary tree structure, sorted that lower numbers are placed
    to the left, while larger numbers are placed to the right.
    """

    def __init__(self):
        super().__init__()

    def add(self, value):

        # If there's no root at all, this is the top of the tree. create node with requested value.
        if self.root is None:
            self.root = Node(value)
            return


        # Check if the value being added is less than that of the root's value.
        if self.root.value >= value:

            # Is there a node already to our left? if not, create a node with the requested value.
            # Otherwise, recurse.
            if self.root.left is None:
                self.root.left = Node(value)
            else:
                self.root = self.root.left
                self.add(value)


        # Value is larger than our root's.
        else:

            # Is there a node already to our right? if not, create a node with the requested value.
            # Otherwise, recurse.
            if self.root.right is None:
                self.root.right = Node(value)
            else:
                self.root = self.root.right
                self.add(value)

    def contains(self, value):
        # method body here
        pass

