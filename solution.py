def bracket_matcher(nput):
    if len(nput) % 2 != 0:
        return False
    checked_string = ''
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    check = []
    for i in nput:
        if i in dict.keys() or i in dict.values():
            checked_string += i
    if len(checked_string) > 0:
        for i in checked_string:
            if i in dict:
                check.append(i)
            else:
                if check == []:
                    return False
                a = check.pop()
                if i != dict[a]:
                    return False
        return check == []
    else:
        return False





print(bracket_matcher('(sdalfkjalskf)'))

print(bracket_matcher('abc(123)'))
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