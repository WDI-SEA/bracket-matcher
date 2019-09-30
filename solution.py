# def bracket_matcher(input):
#   while len(input) > 0:
#     check_string = ''
#     if input[0] == '(':
#         print('hi')
#         if input[len(input) -1] == ')':
#             print('MATCHED')
#             check_string = input(1, len(input) -1)
#             bracket_matcher(check_string)
#         elif input[len(input) - 1] == '' or input[len(input) - 1] == '}':
#             print('Missing closing Parens')
#             return False





#     if  input[0] != '[' or input[0] != '{' or input[0] != '(':
#         check_string = input[1:]
#         print(check_string)
#         bracket_matcher(check_string)
#         return
#     return True

open_brackets = ['(', '[', '{']
close_brackets = [')', ']', '}']

# def bracket_matcher(input):
#     open_bracket_list = []
#     for i in range(len(input)):
#         if input[i] in open_brackets:
#             open_bracket_list.append(input[i])
#             print(open_bracket_list)
#     return open_bracket_list

# def bracket_matcher(input):
#     check_list = bracket_reducer(input)
#     for i in range(len(check_list)):
#         if len(check_list) == 0:
#             return True
#         elif check_list[i] in close_brackets or len(check_list) % 2 != 0:
#             return False
        
#         if check_list[i + 1] in close_brackets and open_brackets.index(check_list[i]) == close_brackets.index(check_list[i + 1]):
#             check_list = 


def bracket_matcher(input):
    open_bracket_list =[]
    for char in input:  
        if char in open_brackets:
            open_bracket_list.append(char)
            print(open_bracket_list)
        elif char in close_brackets:
            if len(open_bracket_list) > 0 and open_bracket_list[len(open_bracket_list) - 1] == open_brackets[close_brackets.index(char)]:
                open_bracket_list.pop()
                print(open_bracket_list)
            else:
                print('False')
                return False

    if len(open_bracket_list) == 0:
        print('True')
        return True
    else:
        print('False')
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
