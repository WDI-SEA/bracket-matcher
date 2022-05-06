from solution import bracket_matcher

print("it should be True",  bracket_matcher('abc(123)'))

# returns true

print("it should be False", bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print("it should be True", bracket_matcher('a[bc(123)]'))
# returns true

print("it should be False", bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print("it should be True", bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print("it should be False", bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print("it should be True", bracket_matcher('()'))
# returns true

print("it should be False", bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print("it should be True", bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched
