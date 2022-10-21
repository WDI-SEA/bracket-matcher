def bracket_matcher(input):
  # list to hold opening 
  for bracket in input:
    print("BRACKET\n", bracket)
    if bracket in open_brackets:
      bracket_stack.append(bracket)
      print("STACK\n", bracket)
      if bracket in open_bracket:
          bracket_stack.append(bracket)
          print("STACK\n", bracket)
      if bracket in close_brackets:
        if len(bracket_stack) < 1
  if close)brackets[bracket] == bracket_stack[len(bracket_stack) - 1]
  if len(bracket_stack) > 0:
    return False
  
  return True

  print("True")
