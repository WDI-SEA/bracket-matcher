def bracket_matcher(input):
  close_brackets = [']', ')', '}']
  open_brackets = ['[', '(', '{']
  check = { '{':'}', '[':']', '(':')' }
  sample_jar = []
  for i in range(len(input)):
    if input[i] in open_brackets:
      sample_jar.append(input[i])
    elif input[i] in close_brackets:
      if len(sample_jar) == 0:
        return False
      else:
        sample = sample_jar.pop()
        if check.get(sample) != input[i]:
          return False
  
  return len(sample_jar) == 0

print('1', bracket_matcher('abc(123)'))
# returns true

print('2', bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print('3', bracket_matcher('a[bc(123)]'))
# returns true

print('4', bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print('5', bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print('6', bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print('7', bracket_matcher('()'))
# returns true

print('8', bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print('9', bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched