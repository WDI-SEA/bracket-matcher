def bracket_matcher(input):
  braces = {'(':')', '[':']', '{':'}'}
  stacked = []
  for each in input:
    if each in braces.keys(): stacked.append(each)
    if each in braces.values():
      try: 
        if braces[stacked.pop()] != each: return False
      except: return False
  if len(stacked) != 0: return False
  else: return True

print(bracket_matcher('(a)'))
print(bracket_matcher('[a(b)]}'))
