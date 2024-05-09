import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation


def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected


def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected


def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected


def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected

#! Note, the following tests were written by me, the student Casey Glidewell.
#? I had noticed that the tests provided were not robust, and have submitted a request
#? for adding these into the testing suite to catch more edge cases.
# def test_nested_extra_characters():
#     actual = multi_bracket_validation("a{b(c[d]e)f}g")
#     expected = True
#     assert actual == expected


# def test_extra_open_round():
#     actual = multi_bracket_validation("(()")
#     expected = False
#     assert actual == expected


# def test_extra_open_square():
#     actual = multi_bracket_validation("[[]")
#     expected = False
#     assert actual == expected


# def test_extra_open_curly():
#     actual = multi_bracket_validation("{{}")
#     expected = False
#     assert actual == expected


# def test_extra_closed_round():
#     actual = multi_bracket_validation("(()))")
#     expected = False
#     assert actual == expected


# def test_extra_closed_square():
#     actual = multi_bracket_validation("[[]]]")
#     expected = False
#     assert actual == expected


# def test_extra_closed_curly():
#     actual = multi_bracket_validation("{{}}}")
#     expected = False
#     assert actual == expected


# def test_woven_brackets():
#     actual = multi_bracket_validation("{(})")
#     expected = False
#     assert actual == expected


# def test_multi_woven_brackets():
#     actual = multi_bracket_validation("({([})])")
#     expected = False
#     assert actual == expected
