# Bracket Matcher

Let's say you're an SEI instructor at GA and you have a student who comes to you with broken code. It's really long, and while trying to find the error, you begin to suspect that there are mismatched parentheses, brackets, or braces. Wouldn't it be nice if you had a function that would take their code as input and return `True` or `False` depending on whether the code was valid? Let's make it happen!

## Directions

* Fork and clone this repository
* Complete the requirements
* Push the answer to your Github and then make a pull request

## Requirements

Write a Python function that takes a string input. This string represents code. It may have any number of characters in it, and the characters may be anything. For our purposes, we'll ignore anything that isn't one of the following: `[`, `]`, `{`, `}`, `(`, `)`. Your function definition looks like this:

```python
def bracket_matcher(input):
```

The return value is a boolean. You should return `True` if the brackets are properly matched and nested, otherwise `False`. 

**HINT**

This problem becomes *remarkably* easier to solve using a recent data structure we've learned in class. Hint, hint!

## Test Cases

```python
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
```
