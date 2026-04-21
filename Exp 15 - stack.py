

stack = []
top = -1


def push(x, n):
    global top
    if top == n - 1:
        print("Stack Overflow")
    else:
        stack.append(x)
        top += 1
        print(f"Inserted {x}")


def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        removed = stack.pop()
        top -= 1
        print(f"Deleted {removed}")

def display():
    if top == -1:
        print("Stack Empty")
    else:
        print("Stack Elements:")
        for i in range(top, -1, -1):
            print(stack[i])


n = int(input("Enter stack size: "))

while True:
    print("\n1.Push\n2.Pop\n3.Display\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        push(x, n)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")