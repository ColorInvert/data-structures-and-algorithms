class BinaryTree:
    """
    Basic binary tree structure. Can output a tree node manifest as an array through either
    pre-order, in-order, or post-order sorting.
    """

    def __init__(self):
        self.root = None
        self.output = []

    # ? A non-recursive, while loop method of getting breadth first ordering of an input
    # ? tree, that uses a list that reads from index 0 to act as a pseudoqueue.


    #! Note that this took lots of re-iterating and a change of the test suite, as my implementation could not pass the required tests as written for unknown reasons. TA assistence provided a new test set, which can be viewed in test_tree_breadth_first.py
    def breadth_first(self):

        # Queue is for storing object references for action ordering...
        queue = []
        # While values is used to hold the values of the nodes themselves.
        values = []

        if not self or self.root is None:
            return[]

        queue.append(self.root)

        # if the queue contains anything...
        while len(queue) > 0:

            node = queue.pop(0)
            # Add front of queue node's value to values list
            values.append(node.value)
            # Set self to node reference at front of queue


            # Check if left exists, and if so
            if node.left is not None:
                queue.append(node.left)

            # Check if right exists, and if so
            if node.right is not None:
                queue.append(node.right)

        return values

    # ? Find and return the largest value present in a binary tree.
    def find_maximum_value(self, node=None):
        # establish tree root
        if node is None:
            node = self.root

            # Establish "highest" value, starting at -infinity so first comparison always
            # leads to an update of value.
            self.highest = float("-inf")

        # Check if we're doing initial setup or not, and skip this check if we are.
        if node is not None:
            # Compare current node value to highest seen, and if node's is bigger, replace.
            if self.highest < node.value:
                self.highest = node.value

        # Check if left exists, and if so, traverse down recursively
        if node.left is not None:
            self.find_maximum_value(node.left)

        # Check if right exists, and if so, traverse down recursively
        if node.right is not None:
            self.find_maximum_value(node.right)

        # Return the value of highest, which should be the highest .value in the tree.
        return self.highest

    # ? Pre order, in order, and post order are the same, except for when the root's
    # ? value is noted down. Before, during or after.

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
    """Protected Tree Node"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# class Node:

#     # Each node can hold it's own value, and the location of the node to its left and right.
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
# Ensure the tests call the method correctly
def breadth_first(tree):
    return tree.breadth_first()
