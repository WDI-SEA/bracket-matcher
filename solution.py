def bracket_matcher(input):
  # Declare lists and dicts for legibility
  open = ['(','[','{']
  close = [')',']','}']
  match_pair = { '(':')', '[':']', '{':'}' }

  # Track current list of brackets
  bracket_list = []

  # Loop through string
  for i in range(len(input)):
    # Check if open bracket
    if input[i] in open:
      bracket_list.append(input[i])
    # Check if closed bracket
    elif input[i] in close:
      # Check if most recent bracket is the matching closing pair
      if len(bracket_list) > 0 and match_pair[bracket_list[-1]] == input[i]:
        bracket_list.pop()
      else:
        return print(False)
    
  # Return False if tracking list is not cleared
  if len(bracket_list) > 0:
    return print(False)

  # Default return value
  return print(True)

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