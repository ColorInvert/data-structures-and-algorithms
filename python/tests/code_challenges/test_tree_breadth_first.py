import pytest
from data_structures.binary_tree import BinaryTree, Node
from code_challenges.tree_breadth_first import breadth_first


#! NOTE: ALTERNATE VERSION OF TESTS PROVIDED BY TA AS RESULT OF HELP TICKET. WAS RUNNING INTO ISSUES WITH EXISTING TESTS EVEN WHILE CONCEPTS BEHIND MY IMPLEMENTATION WERE SOLID.
#! ORIGINAL VERSION OF THE TESTS IS COMMENTED OUT BELOW


def test_exists():
    assert BinaryTree


def test_rootless_tree():
    tree = BinaryTree()
    expected = []
    actual = tree.breadth_first()
    assert actual == expected


def test_single_node():
    tree = BinaryTree()
    tree.root = Node('apples')
    expected = ['apples']
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected


def test_add_two_nodes():
    tree = BinaryTree()
    tree.root = Node('apples')
    tree.root.left = Node('bananas')
    assert tree.root.value == 'apples'
    assert tree.root.left.value == 'bananas'


def test_two_nodes():
    tree = BinaryTree()
    tree.root = Node('apples')
    tree.root.left = Node('bananas')
    expected = ['apples', 'bananas']
    actual = tree.breadth_first()
    assert actual == expected


def test_four_nodes():
    tree = BinaryTree()
    tree.root = Node('apples')
    tree.root.left = Node('bananas')
    tree.root.right = Node('cucumbers')
    tree.root.left.right = Node('dates')
    expected = ['apples', 'bananas', 'cucumbers', 'dates']
    actual = BinaryTree.breadth_first(tree)
    assert actual == expected


# def test_exists():
#     assert breadth_first


# def test_rootless_tree():
#     tree = BinaryTree()
#     expected = []
#     actual = breadth_first(tree)
#     assert actual == expected


# def test_single_node():
#     tree = BinaryTree()
#     tree.root = Node("apples")
#     expected = ["apples"]
#     actual = breadth_first(tree)
#     assert actual == expected


# def test_two_nodes():
#     tree = BinaryTree()
#     tree.root = Node("apples")
#     tree.root.right = Node("bananas")
#     expected = ["apples", "bananas"]
#     actual = breadth_first(tree)
#     assert actual == expected


# def test_four_nodes():
#     tree = BinaryTree()
#     tree.root = Node("apples")
#     tree.root.left = Node("bananas")
#     tree.root.right = Node("cucumbers")
#     tree.root.right.right = Node("dates")
#     expected = ["apples", "bananas", "cucumbers", "dates"]
#     actual = breadth_first(tree)
#     assert actual == expected


# def test_example_from_reading():
#     """
#     We build these out by hand because the example has some gaps
#     i.e. it is not added to left-to-right

#                             2
#                 7                   5
#         2               6                       9
#                     5       11              4

#     result = [2,7,5,2,6,9,5,11,4]
#     """
#     tree = BinaryTree()

#     level_0 = Node(2)
#     level_1_first = Node(7)
#     level_1_second = Node(5)

#     level_2_first = Node(2)
#     level_2_second = Node(6)
#     level_2_third = Node(9)

#     level_3_first = Node(5)
#     level_3_second = Node(11)
#     level_3_third = Node(4)

#     tree.root = level_0
#     level_0.left = level_1_first
#     level_0.right = level_1_second
#     level_1_first.left = level_2_first
#     level_1_first.right = level_2_second
#     level_1_second.right = level_2_third

#     level_2_second.left = level_3_first
#     level_2_second.right = level_3_second

#     level_2_third.right = level_3_third

#     expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
#     actual = breadth_first(tree)

#     assert actual == expected
