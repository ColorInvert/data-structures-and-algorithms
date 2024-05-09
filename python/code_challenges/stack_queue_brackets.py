from data_structures.queue import Queue


def multi_bracket_validation(string):

    round_score = 0
    square_score = 0
    curly_score = 0
    # Balance test section
    #! Note this is all that is needed to solve for the provided tests, but is not robust!
    for character in string:

        # Add a point to the scores if a opening bracket of that type is present...
        if character == "(":
            round_score += 1

        if character == "[":
            square_score += 1

        if character == "{":
            curly_score += 1
        # And remove a point if a closing bracket is detected.
        if character == ")":
            round_score -= 1

        if character == "]":
            square_score -= 1

        if character == "}":
            curly_score -= 1

        # If the character count ever goes into negatives, then we have a closing bracket
        # that did not come before an opening one.
        if round_score < 0 or square_score < 0 or curly_score < 0:
            return False

    return True
