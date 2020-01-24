# Search for regexp anywhere in text
def match(regexp, text):
    if not regexp:
        return True
    if regexp[0] == '^':
        return matchhere(regexp[1:], text)
    for i in range(len(text)):
        if matchhere(regexp, text[i:]):
            return True
    return False

# Search for regexp at beginning of text
def matchhere(regexp, text):
    if not regexp:
        return True
    if len(regexp) > 1 and regexp[1] == '*':
        return matchstar(regexp[0], regexp[2:], text)
    if regexp[0] == '$' and len(regexp) == 1:
        return not text
    if (len(text) > 0 and (regexp[0] == '.' or regexp[0] == text[0])):
        return matchhere(regexp[1:], text[1:])
    return False

# Search for c*regexp at beginning of text
def matchstar(c, regexp, text):
    if matchhere(regexp, text):
        return True
    while(text and (text[0] == c or c == '.')):
        text = text[1:]
        if matchhere(regexp, text):
            return True
    return False

def test():
    print(match('a', 'a') == True)
    print(match('.', 'z') == True)
    # Empty regex matches any text
    print(match('', 'h') == True)
    print(match('a', 'b') == False)
    print(match('p', '') == False)
    print(match('aa', 'aa') == True)
    print(match('a*', 'aa') == True)
    print(match('a*', 'aaa') == True)
    print(match('a*c', 'aaac') == True)
    print(match('^abc', 'abc') == True)
    print(match('bc', 'abc') == True)
    print(match('bc$', 'abc') == True)
    print(match('bc$', 'abca') == False)
    print(match('^a*c', 'aaac') == True)
    print(match('^a*c$', 'aaac') == True)

test()
