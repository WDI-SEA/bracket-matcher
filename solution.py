from inspect import stack


def bracket_matcher(input):
  open_brackets = ['[','(','{']
  close_brackets = [']',')','}']
  stack_list = []
  for i in range(len(input)):
    if input[i] in close_brackets and len(stack_list) == 0:
      return False
    elif input[i] in open_brackets:
      stack_list.append(input[i])
    elif input[i] in close_brackets:
      idx = close_brackets.index(input[i])
      if open_brackets[idx] == stack_list[len(stack_list)-1]:
        stack_list.pop()
      else:
        print(stack_list)
        return False
  if len(stack_list) > 0:
    print(stack_list)
    return False
  return True


print(bracket_matcher('abc(123)'))
# returns true

print(bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns true

print(bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print(bracket_matcher('()'))
# # returns true

print(bracket_matcher('[]]'))
# # returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# # returns true -- no brackets = correctly matched
