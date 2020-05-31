def bracket_matcher(input):
  brackets = {
    ')' : '(', 
    '}' : '{',
    ']' : '[' 
  }

  stack = []
  for char in input: 
    ## if i is an opening bracket, add to stack
    if char in brackets.values(): 
      stack.append(char)
      # if the char from input is in the values of bracket (closing bracket) and the corresponding closing bracket from brackets dictionary is in the stack, pop off 
    elif char in brackets.keys(): 
      if len(stack) > 0 and brackets[char] == stack[-1]: 
        stack.pop()
      else: 
        print(input, 'brackets match- FALSE')
        return False
  if len(stack) > 0:
    print(input, 'brackets match- FALSE')
    return False
  else: 
    print(input, 'brackets match- TRUE')
    return True

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
# # returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched