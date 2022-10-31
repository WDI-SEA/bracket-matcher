def bracket_matcher(input):
  # use a list to hold opening character to determine if a new pair has started
  open_brackets = [ "(", "[", "{" ]
  # use a dictionary to establish the pairs
  close_brackets = {
    ")" : "(",
    "]" : "[",
    "}" : "{"
  }
  # use an empty list variable to store the opening brackets for later comparisons
  bracket_stack = []

  # loop over all of input
  for bracket in input: 
    print("BRACKET\n", bracket)
  # if the current element is a bracket (check our list), then:
    if bracket in open_brackets:
  # push the bracket to our stack variable for later comparisons
      bracket_stack.append(bracket)
      print("STACK\n", bracket_stack)
  # if the current element is a closing bracket (check our dictionary) then
    if bracket in close_brackets:
  # - if the stack variable has no length then the closing bracket current element will never have a match, so return false
      if len(bracket_stack) > 1:
        return False
  # - if the last element in the stack variable is exactly equal to the value associated with the key that is the current element, then return true
      # print("STACK\n", bracket_stack)
      # print("DICT\n", close_brackets)
      if close_brackets[bracket] == bracket_stack[len(bracket_stack) - 1]:
        bracket_stack.pop()

  # if stack variable has a length after the loop is finished, then one bracket didn't have a pair, so return false
  if len(bracket_stack) > 0:
    return False

  # if we made it this far, then it should be all paired up, return true
  return True

  # invoke functionL
print("TRUE", bracket_matcher('a{b}'))