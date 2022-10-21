# input = input('What is your input?\n')

open = ["[","{","("]
closed = ["]","}",")"]

def bracket_matcher(input):
  stack = [] # empty array to stack
  for i in input: # iterate through string
    if i in open: # if any char in the string corresponds to open brackets, append the char in stack array
      stack.append(i)
      print('There is an opening bracket:', i)
    elif i in closed: # if any char string corresponds to closed brackets, make j that char
      j = closed.index(i)
      print('There is an closing bracket:',i)
      # print(open[j])
      if len(stack) > 0 and open[j] == stack[len(stack) - 1]: # if size of stack is > 0 and bracket in open matches saved bracket in stack
        stack.pop() # take the saved bracket out
      else:
        print('FALSE')
        return False # if it doesn't exist, there is no closing bracket
  if len(stack) == 0:
    print('TRUE')
    return True # there is a closing bracket
  else:
    print('FALSE')
    return False # there is no closing bracket

      


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