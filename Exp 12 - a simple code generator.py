
expr = input("Enter expression (Example a+b): ")


a = expr[0]
op = expr[1]
b = expr[2]

print("\nTarget Code")


print(f"MOV R0, {a}")


if op == '+':
    print(f"ADD R0, {b}")
elif op == '-':
    print(f"SUB R0, {b}")
elif op == '*':
    print(f"MUL R0, {b}")
elif op == '/':
    print(f"DIV R0, {b}")
else:
    print("Invalid operator")


print("MOV RESULT, R0")