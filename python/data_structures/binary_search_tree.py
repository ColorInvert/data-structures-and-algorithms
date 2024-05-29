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
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self.root.value

        current = self.root

        # ? Code reworked with TA assistance. Issue seems to have stemmed from not
        # ? pre-defining the new_node value to keep it consistent.

        # Infinite loop
        while True:
            # Is our add value smaller than the current?
            if value < current.value:
                # If there's nothing on the left, put our new node there, return its value.
                if current.left is None:
                    current.left = new_node
                    return current.left.value
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return current.right.value
                current = current.right

    def contains(self, value):

        current = self.root

        # Infinite loop
        while True:

            # Do we have a value match? Return true if so.
            if value == current.value:
                return True

            # Is the value we're looking for smaller than the node's current?
            if value < current.value:
                # Traverse to the left if possible.
                if current.left is not None:
                    current = current.left
                # If left movement is not possible, our value must not be present.
                else:
                    return False

            # Value is bigger than the node's current, and not matching. go right
            # if value exists.
            else:
                # Traverse to the right if possible.
                if current.right is not None:
                    current = current.right
                # If right movement is not possible, our value must not be present.
                else:
                    return False
