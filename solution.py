def bracket_matcher(input):
  opened_brackets = ['[', '{', '(']
  closed_brackets = [']', '}', ')']
  STR = []
  for i in input:
    if i in opened_brackets:
      STR.append(i)
    elif i in closed_brackets:
      complete_bracket = opened_brackets[closed_brackets.index(i)]
      if len(STR) != 0 and STR[-1] == complete_bracket:
        STR.pop()
      else:
        STR.append(i)
  if len(STR) != 0:
    return False
  else:
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
# returns false - no opening bracket to correspond with last character

bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched