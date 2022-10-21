def bracket_matcher(input):
    brackets = []
    opening_brackets = ['{', '[', '(']
    closing_brackets = {  '}': '{',  ']': '[',  ')': '('}
    for i in input:
        if i in opening_brackets:
            brackets.append(i)
        elif i in closing_brackets:
            if len(brackets) > 0:
                if brackets[0] == closing_brackets[i]:
                    brackets.pop()
                else:
                    return False
            else:
                return False
    if len(brackets) > 0:
        return False

    return True


print(bracket_matcher('(h{}{}{}))'))
print(bracket_matcher('()()()()()()()()())'))
print(bracket_matcher('(){}'))

# From read me
print(bracket_matcher('a{b}{c(1[2]3)}'))

print(bracket_matcher('a{b}{c(1}[2]3)'))