from stack import Stack

def par_check(symbol_string):
    stack = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "{[(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False

def matches(open, close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)

print(par_check(""))



