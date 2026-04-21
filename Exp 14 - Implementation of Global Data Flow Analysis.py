
gen = int(input("Enter GEN value: "))
kill = int(input("Enter KILL value: "))
inp = int(input("Enter IN value: "))


out = gen + (inp - kill)

print("\nData Flow Equation")
print("OUT[B] = GEN[B] U (IN[B] - KILL[B])")

print(f"\nComputed OUT value: {out}")