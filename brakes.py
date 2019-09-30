def bracket_matcher(input):
    #need two global lists to check after we read the initial input.
    right_facing = []
    left_facing = []
    # we also need to parse the string into its own list for reading off
    input_list = list(input)
    # parse throught the input, and push into either left or right facing
    for value in input:
        if value == '(' or value == '{' or value == '[':
            right_facing.append(value)
        if value == ')' or value == '}' or value == ']':
            left_facing.append(value)
            # for the left facing value, there might be a match here. We need to check to see if there is a corresponding value
            # index for match target
            last_right_index = len(right_facing) - 1
            # check to see if the right facing ones even have a
            if last_right_index >= 0:
                r = right_facing[last_right_index]
                if r == '(' and left_facing[0] == ')':
                    right_facing.pop()
                    left_facing.pop()
                if r == '{' and left_facing[0] == '}':
                    right_facing.pop()
                    left_facing.pop()
                if r == '[' and left_facing[0] == ']':
                    right_facing.pop()
                    left_facing.pop()
    if len(right_facing) == 0  and len(left_facing) == 0:
        print('true')
        return True
    else:
        print('false')
        return False







bracket_matcher('abc(123)')
# returns true

bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

bracket_matcher('a[bc(123)]')
# returns true

bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

bracket_matcher('a{b}{c(1[2]3)}')
# returns true

bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

bracket_matcher('()')
# returns true

bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched
