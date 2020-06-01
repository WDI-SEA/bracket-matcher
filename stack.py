def bracket_matcher(input):
    brackets = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
    }
    stack = []
    for char in input:
        if char in brackets.value() or char in brackets.keys():
            stack.append(char)
    print(stack)
    if stack % 2 != 0:
        print(input, "brackets don't match!")
        return False
    else: 
        print('Idk')



# bracket_matcher('abc(123)')
# returns true

# bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

# bracket_matcher('a[bc(123)]')
# returns true

# bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

# bracket_matcher('a{b}{c(1[2]3)}')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

# bracket_matcher('()')
# returns true

# bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

# bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched
