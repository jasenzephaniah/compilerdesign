


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def is_operator(c):
    return c in ['+', '-', '*', '/', '^']


def infix_to_postfix(expression):
    stack = []
    output = []

    tokens = expression.split()

    for token in tokens:
        
        if token.isalnum():
            output.append(token)

        
        elif token == '(':
            stack.append(token)

        
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  

        
        else:
            while (stack and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)

    
    while stack:
        output.append(stack.pop())

    return ' '.join(output)



def infix_to_prefix(expression):
    
    tokens = expression.split()[::-1]


    for i in range(len(tokens)):
        if tokens[i] == '(':
            tokens[i] = ')'
        elif tokens[i] == ')':
            tokens[i] = '('

    reversed_expr = ' '.join(tokens)

    
    postfix = infix_to_postfix(reversed_expr)

    
    prefix = postfix.split()[::-1]

    return ' '.join(prefix)



expr = input("Enter infix expression (space-separated): ")

postfix = infix_to_postfix(expr)
prefix = infix_to_prefix(expr)

print("\nPostfix Expression:", postfix)
print("Prefix Expression :", prefix)