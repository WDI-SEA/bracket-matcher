def bracket_matcher(input):
    open_brackets = ["(", "[", "{"]
    close_brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    bracket_stack = []
    for bracket in input:
        print("bracket: ", bracket)
        if bracket in open_brackets:
            bracket_stack.append(bracket)
        if bracket in close_brackets:
            if len(bracket_stack) < 1:
                return False
            if close_brackets[bracket] == bracket_stack[len(bracket_stack)-1]:
                bracket_stack.pop()
    if len(bracket_stack) > 0:
        return False
    return True


print(bracket_matcher('abc(123)'))
