def bracket_matcher(input):
  # Use a list to define the empty stack
  stack = []

  # Loop over the string and check for opening brackets
  for i in input:
    if i in ['(', '{', '[']:
      # Push opening brackets to the stack
      stack.append(i)
      # print(stack)
    elif i in [')', '}', ']']:
      # Find closing brackets
      if len(stack) == 0:
        # If there are closing brackets and no opening brackets, return false
        print('False')
        return False
      elif len(stack) > 0 and i in [')', '}', ']']:
        # If there are opening brackets, check for a match, then pop the matching opening bracket
        if i == ')' and stack[-1] == '(' or i == '}' and stack[-1] == '{' or i == ']' and stack[-1] == '[':
          # print(i)
          # print(stack[-1])
          stack.pop()
          # print(stack)     
    
  if len(stack) == 0:
    # Stack will be zero if brackets match
    print('True')
    return True
  else:
    # Brackets do not match if the length of the stack is not zero
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