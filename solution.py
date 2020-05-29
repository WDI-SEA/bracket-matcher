def bracket_matcher(input):
  pass
  brackets = ['[','{','(',']','}',')']

  c = ''
  stack = []

  for c in input:
    if c in brackets:
      if len(stack) == 0:
        stack.append(c)
      else:
        if stack[len(stack) - 1] == '[' and c == ']':
          stack = stack[:-1]  
        elif stack[len(stack) - 1] == '{' and c == '}':
          stack = stack[:-1]  
        elif stack[len(stack) - 1] == '(' and c == ')':
          stack = stack[:-1]
        else:
          stack.append(c)

  if len(stack) > 0:
    return False
  else:
    return True


print(f"{bracket_matcher('[t[e]s]t')}")
# returns true

print(f"{bracket_matcher('abc(123)')}")
# returns true

print(f"{bracket_matcher('a[b]c(123')}")
# returns false -- missing closing parens

print(f"{bracket_matcher('a[bc(123)]')}")
# returns true

print(f"{bracket_matcher('a[bc(12]3)')}")
# returns false -- improperly nested

print(f"{bracket_matcher('a{b}{c(1[2]3)}')}")
# returns true

print(f"{bracket_matcher('a{b}{c(1}[2]3)')}")
# returns false -- improperly nested

print(f"{bracket_matcher('()')}")
# returns true

print(f"{bracket_matcher('[]]')}")
# returns false - no opening bracket to correspond with last character

print(f"{bracket_matcher('abc123yay')}")
# returns true -- no brackets = correctly matched