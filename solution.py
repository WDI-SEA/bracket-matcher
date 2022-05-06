

def bracket_matcher(input):
    # stack to keep track of brackets
    brackets = []
    # need to know all valid characters
    opening_chars = ['{', '[', '(']
    closing_chars = {
            '}': '{', 
            ']': '[', 
            ')': '('
            }
    # edge case where input is empty string
    if len(input) == 0:
        return True
    # edge case where last thing in string is an opening bracket
    if input[len(input) - 1] in opening_chars:
        return False

    # loop over input and check if char is a valid character
    for char in input:
        # if it is opening, add to stack
        if char in opening_chars:
            brackets.insert(0, char)
        # else if it is closing check, make sure it has a matching closing first in the stack
        elif char in closing_chars:
            if len(brackets) > 0:
                if brackets[0] == closing_chars[char]:
                    # if so, pop it off the stack and keep going 
                    brackets = brackets[1:]
                else:
                    # if not, return false, because it is a mismatch
                    return False
            else:
                # we are trying to match a bracket and the stack is empty
                return False
    
    # if there is anything in the stack -- return false
    if len(brackets) > 0:
        return False

    return True

if __name__ == '__main__':
    # print(bracket_matcher('(hello)'))
    print('it should be False:', bracket_matcher('(h))'))
    print('it should be True:',  bracket_matcher('()'))

    print('it should be False:',  bracket_matcher('{} () (({hello})) [()] {'))
    print('it should be True:', bracket_matcher('{} () (({hello})) [()]'))
    print('it should be True:', bracket_matcher(''))
