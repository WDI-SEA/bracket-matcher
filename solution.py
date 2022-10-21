
def bracket_matcher(input):
  open_brackets = ["[", "{", "("]
  closed_brackets = ["]", "}", ")"]
  string = []
  for i in input:
    if i in open_brackets:
      # if i matches with the open brackets then put it in the string
      string.append(i)
    elif i in closed_brackets:
      # matching the indices 
      match = open_brackets[closed_brackets.index(i)]
      if len(string) != 0 and string[-1] == match:
        string.pop()
      else:
        string.append(i)
  if len(string) != 0:
    return False
  else:
    return True


  

print(bracket_matcher("abc(123)"))
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
# returns true

print(bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched
