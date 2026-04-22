from collections import defaultdict

grammar = {
    "E": ["T E'"],
    "E'": ["+ T E'", "ε"],
    "T": ["F T'"],
    "T'": ["* F T'", "ε"],
    "F": ["( E )", "id"]
}

FIRST = {
    "E": {"(", "id"},
    "E'": {"+", "ε"},
    "T": {"(", "id"},
    "T'": {"*", "ε"},
    "F": {"(", "id"}
}

FOLLOW = {
    "E": {")", "$"},
    "E'": {")", "$"},
    "T": {"+", ")", "$"},
    "T'": {"+", ")", "$"},
    "F": {"*", "+", ")", "$"}
}

table = defaultdict(dict)

for A in grammar:
    for production in grammar[A]:
        first_alpha = set()

        symbols = production.split()

        
        for sym in symbols:
            if sym in FIRST:
                first_alpha |= (FIRST[sym] - {"ε"})
                if "ε" not in FIRST[sym]:
                    break
            else:
                first_alpha.add(sym)
                break
        else:
            first_alpha.add("ε")

      
        for terminal in first_alpha:
            if terminal != "ε":
                table[A][terminal] = production

        
        if "ε" in first_alpha:
            for terminal in FOLLOW[A]:
                table[A][terminal] = production


print("\nPredictive Parsing Table:\n")

for nt in table:
    for t in table[nt]:
        print(f"M[{nt}, {t}] = {nt} -> {table[nt][t]}")