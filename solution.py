

def bracket_matcher(input):
    # stack to keep track of brackets
    # need to know all valid characters

    # loop over input and check if char is a valid character
        # if char is a valid character check if it is opening
            # if it is opening, add to stack
            # else if it is closing check, make sure it has a matching closing first in the stack
                # if so, pop it off the stack and keep going 
                # if not, return false, because it is a mismatch
