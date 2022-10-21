
open_bracket = ["{", "[", "("]
close_bracket= [ "}", "]", ")"]

def bracket_matcher(input):
    # set empty stack
    stack = []
    # iterate through the array to search for open brackets
    for i in input:
        # if open is in the array move it to the stack
        if i in open_bracket:
            stack.append[i]
            print (stack[i])
        # if not save the index so you can compare to in the stack
        elif i in close_bracket:
            closed = close_bracket[i] 
        # if the closed[i] is in stack then pop open from stack
    if closed == stack[i]:
        stack.pop[i]
        return True
        # if its not then leave open in stack
    else:
        return False
     # if stack is empty - brackets are all matched and return true

    # if stack is not empty - there are unmatched brackets return false

    # bracket_matcher('[]]')


# -----------------------------  code along solution  -----------------------------

def bracket_matcher(input):
    # use a list to hold opening char to determine if new pair has 
    open_brackets = ["{", "[", "("]
    # use dictionary to est pairs
    close_brackets= {
         "}" :"{", 
         "]": "]", 
         ")": "("
    }
    #  use empty list var to store opening brackets for later comparisons
    stack =[]
    # want to loop over input
    for bracket in input:
        # print("Bracket:", bracket)
        # if current char is a bracket check list,
        if bracket in open_brackets:
             # then push bracket to stack 
            stack.append(bracket)
            print("Stack: " ,stack)
        #  if current char is closing bracket (check dict) then
        if bracket in close_brackets:
            # if the stack  has no length then the closing bracket wont have a match
            if len(stack) < 1:
                # return false
                return False
            # print("STACK: ", stack)
            # print ("DICT: ", close_brackets[bracket])
            #  if the last char in stack  == current char
            if close_brackets[bracket] == stack[len(stack)-1]:
                # pop from stack
                stack.pop()
    # if after looping through input stack has length
    if len(stack) > 0:
        # return false
        return False
        # else return true
    return True

print(bracket_matcher("({a})"))
print(bracket_matcher('a{b}{c(1}[2]3)'))