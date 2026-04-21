

from collections import defaultdict, deque

grammar = defaultdict(list)
non_terminals = set()
terminals = set()


n = int(input("Enter number of productions: "))

print("Enter productions (Example: E -> E + T | T):")
for _ in range(n):
    prod = input()
    lhs, rhs = prod.split("->")
    lhs = lhs.strip()
    non_terminals.add(lhs)

    for alt in rhs.split("|"):
        symbols = alt.strip().split()
        grammar[lhs].append(symbols)

        for sym in symbols:
            if not sym.isupper():
                terminals.add(sym)
            else:
                non_terminals.add(sym)


start_symbol = list(grammar.keys())[0]
augmented_start = start_symbol + "'"
grammar[augmented_start] = [[start_symbol]]
non_terminals.add(augmented_start)

def closure(items):
    closure_set = set(items)

    while True:
        new_items = set(closure_set)

        for (lhs, rhs, dot) in closure_set:
            if dot < len(rhs):
                symbol = rhs[dot]

                if symbol in non_terminals:
                    for prod in grammar[symbol]:
                        item = (symbol, tuple(prod), 0)
                        if item not in new_items:
                            new_items.add(item)

        if new_items == closure_set:
            break

        closure_set = new_items

    return frozenset(closure_set)


def goto(items, symbol):
    moved = []

    for (lhs, rhs, dot) in items:
        if dot < len(rhs) and rhs[dot] == symbol:
            moved.append((lhs, rhs, dot + 1))

    return closure(moved)


C = []
start_item = closure([(augmented_start, tuple(grammar[augmented_start][0]), 0)])

C.append(start_item)

queue = deque([start_item])
transitions = {}

while queue:
    I = queue.popleft()

    for symbol in list(terminals | non_terminals):
        g = goto(I, symbol)

        if g and g not in C:
            C.append(g)
            queue.append(g)

        if g:
            transitions[(C.index(I), symbol)] = C.index(g) if g in C else len(C) - 1

def print_item(item):
    lhs, rhs, dot = item
    rhs = list(rhs)
    rhs.insert(dot, "•")
    return f"{lhs} -> {' '.join(rhs)}"

print("\nLR(0) Item Sets:\n")

for i, state in enumerate(C):
    print(f"I{i}:")
    for item in state:
        print(" ", print_item(item))
    print()

print("Transitions (GOTO):\n")
for (state, symbol), target in transitions.items():
    print(f"I{state} -- {symbol} --> I{target}")