class Node:
	def __init__(self, char, next):
		self.char = char
		self.next = next
	def __str__(self):
		return f"{self.char}"

class Stack:
	def __init__(self):
		self.head = None
		self.size = 0
	def __str__(self):
		string = "[ "
		curr_node = self.head
		while curr_node:
			string += f"{curr_node} -> "
			curr_node = curr_node.next
		return string + "None ]"
	def push(self, char):
		self.head = Node(char, self.head)
		self.size += 1
	def pop(self):
		popped_node = self.head
		self.head = self.head.next
		self.size -= 1
		return popped_node
	def peek(self):
		return f"{self.head}"

def bracket_matcher(input):
	open_brackets = { "(": ")", "[": "]", "{": "}" }
	close_brackets = { ")": "(", "]": "[", "}": "{" }
	my_stack = Stack()
	for char in input:
		if char in open_brackets:
			my_stack.push(char)
		elif char in close_brackets:
			if my_stack.peek() == close_brackets[char]:
				my_stack.pop()
			else:
				return False
	return not my_stack.size > 0

print(bracket_matcher("abc(123)"))     	    # expects true
print(bracket_matcher("a[b]c(123"))   	    # expects false - missing closing ')'
print(bracket_matcher("a[bc(123)]"))		# expects true
print(bracket_matcher("a[bc(12]3)"))		# expects false - improperly nested
print(bracket_matcher("a{b}{c(1[2]3)}"))	# expects true
print(bracket_matcher("a{b}{c(1}[2]3)"))	# expects false - improperly nested
print(bracket_matcher("()"))			    # expects true
print(bracket_matcher("[]]"))			    # expects false - no opening bracket to correspond with last character
print(bracket_matcher("abc123yay"))			# expects true - no brackets = correctly matched
