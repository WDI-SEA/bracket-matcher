def bracket_matcher(input):
  open_brackets = [ "(", "[", "{" ]
  close_brackets = {
    ")": "(",
    "]": "[",
    "}": "{"
  }

  bracket_stack = []

  for bracket in input:
    if bracket in open_brackets:
      bracket_stack .append(bracket)

    if bracket in close_brackets:

      if len(bracket_stack) < 1:
        return False
    if close_brackets[bracket] == bracket_stack[len(bracket_stack) - 1]:
      bracket_stack.pop()
  if len(bracket_stack) > 0:
    return False
  return True




# ```python
print(bracket_matcher('abc(123)'))
# # returns true

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
# ```