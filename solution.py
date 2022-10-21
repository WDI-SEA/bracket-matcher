# def bracket_matcher(input):
  # stack = []
 
  # for char in input:
  #     if char in ["(", "{", "["]:
 
  #       # Push the element in the stack
  #       stack.append(char)
  #     else:
 
  #     # IF current character is not opening
  #     # bracket, then it must be closing.
  #     # So stack cannot be empty at this point.
  #       if not stack:
  #         return False
  #         current_char = stack.pop()
  #       if current_char == '(':
  #       if char != ")":
  #         return False
  #       if current_char == '{':
  #       if char != "}":
  #         return False
  #       if current_char == '[':
  #       if char != "]":
  #         return False


def bracket_matcher(input):
  # use a list to hold opening character to determine if a new pair has started
  open_brackets = ["(", "[", "{"]
  # use a dictionary to establish the pairs 
  close_brackets = {
    ")": "(",
    "]": "[",
    "}": "{"
  }
  # use a empty list variable to store the opening bracket for later comparisons
  bracket_stack = []

  # loop over all of input
  for bracket in input:
    print ("BRACKET\n", bracket)
    # if the current element is a bracket (check our list) then
    if bracket in open_brackets:
      # push the bracket to our stack variable for later comparisons
      bracket_stack.append(bracket)
      print("STACK\n", bracket_stack)
    # if the current element is a closing bracket (check our dictionary) then
    if bracket in close_brackets:
      # - if the stack variable has no length then the closing bracket current element will never have a match so return false
      if len(bracket_stack) < 1:
        return False
      # - if the last element in the stack variable is exactly equal to the value associated with the key that is the current element, then pop from bracket stack so it doesn't confuse future comparisons
      print("STACK\n", bracket_stack)
      print("DICT\n", close_brackets[bracket])
      if close_brackets[bracket] == bracket_stack[len(bracket_stack) - 1]:
        bracket_stack.pop()

  # if stack variable has a length after the loop is finished, then one bracket didn't have a pair so return false
  if len(bracket_stack) > 0:
    return False

  # if we made it this far, then it should be all paired up , return true
  return True


 # invoke the function
# bracket_matcher('({a})')
print(bracket_matcher('a{b}{c(1[2]3)}'))
# should return true

print(bracket_matcher('a{b}{c(1}[2]3)'))
#false
