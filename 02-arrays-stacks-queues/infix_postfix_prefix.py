"""
Topic: Infix, prefix, postfix conversion and evaluation (Module 2, high priority)
Problem: Convert infix -> postfix/prefix and evaluate a postfix expression.
Source: Classic
Difficulty: Medium
Approach: Infix->postfix with a stack:
            operand -> output; '(' -> push; ')' -> pop to output until '(';
            operator -> pop operators of higher (or equal, if left-associative)
            precedence, then push; at the end pop everything.
          Postfix->prefix: stack of strings, op + a + b.
          Evaluate postfix: push operands; on an operator pop b then a, push a op b.
Time: O(n)   Space: O(n)
"""

PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(expr):
    out, stack = [], []
    for ch in expr.replace(" ", ""):
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack[-1] != "(":
                out.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != "("
                   and (PREC[stack[-1]] > PREC[ch]
                        or (PREC[stack[-1]] == PREC[ch] and ch != "^"))):
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    return "".join(out)


def postfix_to_prefix(post):
    stack = []
    for ch in post:
        if ch.isalnum():
            stack.append(ch)
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(ch + a + b)
    return stack[0]


def infix_to_prefix(expr):
    return postfix_to_prefix(infix_to_postfix(expr))


def evaluate_postfix(tokens):
    """tokens: space separated string, e.g. '8 2 3 * + 4 -'"""
    stack = []
    for t in tokens.split():
        if t in PREC:
            b, a = stack.pop(), stack.pop()
            stack.append({"+": a + b, "-": a - b, "*": a * b,
                          "/": a / b, "^": a ** b}[t])
        else:
            stack.append(float(t))
    return stack[0]


if __name__ == "__main__":
    assert infix_to_postfix("A+B*C") == "ABC*+"
    assert infix_to_prefix("A+B*C") == "+A*BC"
    assert infix_to_postfix("(A+B)*C") == "AB+C*"
    assert infix_to_postfix("A-B-C") == "AB-C-"        # left associative
    assert infix_to_postfix("A^B^C") == "ABC^^"        # right associative
    assert evaluate_postfix("8 2 3 * + 4 -") == 10
    print("OK")
