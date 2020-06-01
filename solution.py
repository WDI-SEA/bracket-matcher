def bracket_matcher(input):
    brackets = {
        #(keys) : (values)
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []  # empty array that were going to match are parantheses with
    for char in input:
        print('This is my stack', stack, 'length of stack is', len(stack))
        if char in brackets.values():
            stack.append(char)
            print('Stack of opening brackets', stack)
        elif char in brackets.keys() and brackets[char] == stack[-1]:
            print(stack[-1:])
            stack.pop()

    if len(stack) > 0:
        print(input, 'brackets match - FALSE')
        return False
    else:
        print(input, 'brackets match - TRUE')
        return True


bracket_matcher('abc(123)')
# returns true

# bracket_matcher('a[b]c(123')
# # returns false -- missing closing parens

# bracket_matcher('a[bc(123)]')
# # returns true

# bracket_matcher('a[bc(12]3)')
# # returns false -- improperly nested

# bracket_matcher('a{b}{c(1[2]3)}')
# # returns true

# bracket_matcher('a{b}{c(1}[2]3)')
# # returns false -- improperly nested

# bracket_matcher('()')
# # returns true

# bracket_matcher('[]]')
# # returns false - no opening bracket to correspond with last character

# bracket_matcher('abc123yay')
# # returns true -- no brackets = correctly matched
