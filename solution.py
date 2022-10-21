def bracket_matcher(input):
	# bracket references
	opening_brackets = ["[", "{", "("]
	closing_brackets = {
		"]": "[",
		"}": "{",
		")": "("
	}
	# stack to keep track of brackets in input
	bracket_stack = []
	# loop over input
	for char in input:
		# if opening bracket
		if char in opening_brackets:
			# append to stack
			bracket_stack.append(char)
		# if closing bracket
		elif char in closing_brackets:
			# check if stack is empty
			if len(bracket_stack) == 0:
				# and append bracket if it is
				bracket_stack.append(char)
			# check top of stack for matching opening bracket
			# if top of stack equals matching opening bracket
			elif bracket_stack[-1] == closing_brackets[char]:
				# pop it off
				bracket_stack.pop()
			# else append the closing bracket
			else:
				bracket_stack.append(char)
		else:
			continue

	# if there are still brackets in our stack
	if len(bracket_stack) > 0:
		# there were mismatched brackets and we can return false
		return print(False)
	# else when our bracket stack is empty
	else:
		# all brackets were matched! we can return true
		return print(True)

def optimized_bracket_matcher(input):
	# brackets reference
	opening_brackets = ["[", "{", "("]
	closing_brackets = {
		"]": "[",
		"}": "{",
		")": "("
	}
	# stack for keeping track of brackets in input
	bracket_stack = []
	# loop over characters in input
	for char in input:
		# if a closing bracket
		if char in closing_brackets:
			# if stack is empty
			if len(bracket_stack) == 0:
				# we can return false (this bracket has no opening)
				return print(False)
			# else if top of stack matches opening bracket for current closing bracket
			elif bracket_stack[-1] == closing_brackets[char]:
				# pop off top of stack
				bracket_stack.pop()
			# else we can return false (top of stack does not match current closing bracket)
			else: return print(False)
		# if opening bracket
		elif char in opening_brackets:
			# push to stack
			bracket_stack.append(char)
	
	# if we make it down here and the stack is empty
	if len(bracket_stack) == 0:
		# return true (all our brackets were matched!)
		return print(True)
	# else return false (a bracket was never closed)
	else: return print(False)


# test cases #
optimized_bracket_matcher('abc(123)')
# returns true

optimized_bracket_matcher('a[b]c(123')
# returns false -- missing closing parens

optimized_bracket_matcher('a[bc(123)]')
# returns true

optimized_bracket_matcher('a[bc(12]3)')
# returns false -- improperly nested

optimized_bracket_matcher('a{b}{c(1[2]3)}')
# returns true

optimized_bracket_matcher('a{b}{c(1}[2]3)')
# returns false -- improperly nested

optimized_bracket_matcher('()')
# returns true

optimized_bracket_matcher('[]]')
# returns false - no opening bracket to correspond with last character

optimized_bracket_matcher('abc123yay')
# returns true -- no brackets = correctly matched