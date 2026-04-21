

def check_reduce(stack):
    
    s = ''.join(stack)


    if s.endswith('id'):
        return ('id', 'E')

    if s.endswith('E+E'):
        return ('E+E', 'E')

    if s.endswith('E*E'):
        return ('E*E', 'E')

    if s.endswith('(E)'):
        return ('(E)', 'E')

    return None


def shift_reduce_parser(input_string):
    
    tokens = input_string.replace('id', 'i').replace(' ', '')
    tokens = list(tokens)
    tokens.append('$')

    stack = ['$']

    print(f"{'Stack':<20}{'Input':<20}{'Action'}")
    print("-" * 50)

    i = 0
    while True:
        current_input = ''.join(tokens[i:])

      
        reduced = check_reduce(stack)

        if reduced:
            rhs, lhs = reduced
            print(f"{''.join(stack):<20}{current_input:<20}Reduce {lhs}->{rhs}")

            
            for _ in range(len(rhs)):
                stack.pop()

            
            stack.append(lhs)

        elif i < len(tokens):
          
            print(f"{''.join(stack):<20}{current_input:<20}Shift")
            stack.append(tokens[i])
            i += 1

        else:
            break

        
        if stack == ['$', 'E'] and tokens[i] == '$':
            print(f"{''.join(stack):<20}{tokens[i]:<20}Accept")
            break

input_expr = input("Enter expression (use id, +, *, parentheses): ")
shift_reduce_parser(input_expr)