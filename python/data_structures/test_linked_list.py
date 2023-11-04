from linked_list import Node
from linked_list import LinkedList

#?Can we make a node?
def test_node_1():
    actual = Node(1)
    expected = 1
    assert actual.value == expected


#?Can we make a node that points to another?
def test_node_next():
    node1 = Node(1)
    node2 = Node(2, node1)
    actual = node2.next
    expected = node1
    assert actual == expected


# ?Check for a none error when getting the head of a created list. if an error is caught when trying, none_error becomes true, which is what the assert is looking for.
def test_create_empty():
    my_list = LinkedList()
    try:
        actual = my_list.head()
    except:
        none_error = True

    assert none_error == True


#? When we make a linked list and call the method insert with a value, is a new node with that value put into the linked list as the head?
def test_insert_adds_to_start():
    my_list = LinkedList()
    my_list.insert(23)

    actual = my_list.head.value
    expected = 23
    assert actual == expected

#? When we make a linked list and call the method insert with a value multiple times, is hte head updating to the latest insert call, with a next pointing to the previous head?
def test_insert_points_to_next():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)

    current = my_list.head
    actual = current.value
    expected = 2
    assert actual == expected

#? does the "includes" method accurately respond true for items inserted first (at the end of the list?)
def test_includes_accurate_hit_start():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(1)
    expected = True
    assert actual == expected

#? does the "includes" method accurately respond true for items inserted somewhere in the middle?
def test_includes_accurate_hit_mid():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(2)
    expected = True
    assert actual == expected

#? does the "includes" method accurately respond true for items inserted last?
def test_includes_accurate_hit_end():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(3)
    expected = True
    assert actual == expected

#? does the "includes" method accurately respond false for values not present?
def test_includes_accurate_miss():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.includes(3235)
    expected = False
    assert actual == expected


#?Test below passed mid development. not sure how to healthily keep this test implemented without damaging the purpose of to_string, as this is a test of the middle step of to_string's function.
# def test_to_string_captures_values():
#     my_list = LinkedList()
#     my_list.insert(1)
#     my_list.insert(2)
#     my_list.insert(3)

#     actual = my_list.to_string()
#     expected = [3, 2, 1]
#     assert actual == expected



#? Does to_string return a string value matching the required formatting?
def test_to_string():
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    actual = my_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected


# TODO:

#! Write tests to prove the following functionality:

#!     Can successfully instantiate an empty linked list
#!     Can properly insert into the linked list
#!     The head property will properly point to the first node in the linked list
#!     Can properly insert multiple nodes into the linked list
#!     Will return true when finding a value within the linked list that exists
#!     Will return false when searching for a value in the linked list that does not exist
#!     Can properly return a collection of all the values that exist in the linked list
