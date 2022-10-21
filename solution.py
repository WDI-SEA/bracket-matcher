
open = ["{", "[", "("]
closed = [ "}", "]", ")"]

def bracket_matcher(input):
    # set empty stack
    stack = []
    # iterate through the array to search for open brackets
    for i in input:
        # if open is in the array move it to the stack
        if i in open:
            stack.append(i)
        # if not save the index so you can compare to in the stack
        elif i in closed:
            closed[i] 
        # if the closed[i] is in stack then pop open from stack
        # if its not then leave open in stack

    # if stack is empty - brackets are all matched and return true
    # if stack is not empty - there are unmatched brackets return false