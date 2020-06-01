open_brack = ['(', '{', '[']
closed_brack = [')', '}', ']']
# index_of_open = 0
# index_of_close = 0

def bracket_matcher(input):
    stacked = []
    for key in input:
        if key in open_brack: 
            stacked.append(key)
            # index_of_open = open_brack.index(key)
            # print(stacked)
        elif key in closed_brack: 
            # index_of_close = closed_brack.index(key)
            open_match = open_brack[closed_brack.index(key)]
            print('stacked: ', stacked[-1], 'open_match: ', open_match)
            if stacked[-1] == open_match:
                stacked.pop()
                # print(stacked)
            else:
                stacked.append(key)
            print(stacked)
    if len(stacked) != 0:
        print('False')
    else: 
        print('True')
# brackets = {
#     '}': '{',
#     ']': '[',
#     ')': '('
# }



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

# bracket_matcher('[}]')
# # returns false - no opening bracket to correspond with last character

# bracket_matcher('abc123yay')
# # returns true -- no brackets = correctly matched

# 

# def bracket_matcher(input):
#     stacked = []
#     for key in input:
#         # if i is an opening bracket
#         if key in brackets.values():
#             # add to stacked
#             stacked.append(key)
#         # if key is a closing bracket and the opening bracket is in stacked
#         # if key in brackets.keys() and key in stacked:
#         #     stacked.pop()
#         elif key in brackets.keys(): 
#             if len(stacked) > 0 and brackets[key] == stacked[-1]:
#                 print('brackets at da key',brackets[key]) 
#                 stacked.pop()
#             else: 
#                 print(input, 'brackets match- FALSE')
#                 return False
#     if len(stacked) > 0:
#         print(input, 'brackets match- FALSE')
#         return False
#     else: 
#         print(input, 'brackets match- TRUE')
#         return True