import pytest
from data_structures.stack import Stack
from data_structures.stack import PseudoQueue
from data_structures.invalid_operation_error import InvalidOperationError

#?Tests for PseudoQueue are near the bottom, and the beginning of them is marked.
def test_exists():
    assert Stack


def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected



def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected



def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"



def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"


#? Begin PseudoQueue tests

def test_pseudo_queue_in_out():
    p = PseudoQueue()
    p.enqueue("banana")
    p.enqueue("apple")
    actual = p.dequeue()
    expected = "banana"
    assert actual == expected


def test_pseudo_dequeue_empty():
    p = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        p.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"

def test_pseudo_dequeue_too_many():
    p = PseudoQueue()
    p.enqueue("banana")
    p.enqueue("apple")
    p.dequeue()
    p.dequeue()
    with pytest.raises(InvalidOperationError) as e:
        p.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"
