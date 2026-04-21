

from collections import defaultdict


grammar = defaultdict(list)

def add_production(lhs, rhs_list):
    for rhs in rhs_list:
        grammar[lhs].append(rhs.strip())


def compute_leading():
    leading = defaultdict(set)

    changed = True
    while changed:
        changed = False

        for lhs in grammar:
            for rhs in grammar[lhs]:
                symbols = rhs.split()

        
                if symbols[0].islower() or not symbols[0].isalpha():
                    if symbols[0] not in leading[lhs]:
                        leading[lhs].add(symbols[0])
                        changed = True

                
                else:
                    for sym in leading[symbols[0]]:
                        if sym not in leading[lhs]:
                            leading[lhs].add(sym)
                            changed = True

                if len(symbols) > 1:
                    if symbols[0].isupper() and (symbols[1].islower() or not symbols[1].isalpha()):
                        if symbols[1] not in leading[lhs]:
                            leading[lhs].add(symbols[1])
                            changed = True

    return leading


def compute_trailing():
    trailing = defaultdict(set)

    changed = True
    while changed:
        changed = False

        for lhs in grammar:
            for rhs in grammar[lhs]:
                symbols = rhs.split()

               
                if symbols[-1].islower() or not symbols[-1].isalpha():
                    if symbols[-1] not in trailing[lhs]:
                        trailing[lhs].add(symbols[-1])
                        changed = True

               
                else:
                    for sym in trailing[symbols[-1]]:
                        if sym not in trailing[lhs]:
                            trailing[lhs].add(sym)
                            changed = True

                
                if len(symbols) > 1:
                    if symbols[-1].isupper() and (symbols[-2].islower() or not symbols[-2].isalpha()):
                        if symbols[-2] not in trailing[lhs]:
                            trailing[lhs].add(symbols[-2])
                            changed = True

    return trailing



n = int(input("Enter number of productions: "))

print("Enter productions (format: E -> E + T):")
for _ in range(n):
    prod = input()
    lhs, rhs = prod.split("->")
    lhs = lhs.strip()
    rhs_list = rhs.split("|")
    add_production(lhs, rhs_list)



leading = compute_leading()
trailing = compute_trailing()


print("\nLEADING sets:")
for nt in leading:
    print(f"{nt} : {{ {', '.join(leading[nt])} }}")

print("\nTRAILING sets:")
for nt in trailing:
    print(f"{nt} : {{ {', '.join(trailing[nt])} }}")