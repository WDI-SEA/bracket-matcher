def bracket_matcher(input):
  stack = []
 
  for char in input:
      if char in ["(", "{", "["]:
 
        # Push the element in the stack
        stack.append(char)
      else:
 
      # IF current character is not opening
      # bracket, then it must be closing.
      # So stack cannot be empty at this point.
        if not stack:
          return False
          current_char = stack.pop()
        if current_char == '(':
        if char != ")":
          return False
        if current_char == '{':
        if char != "}":
          return False
        if current_char == '[':
        if char != "]":
          return False

 