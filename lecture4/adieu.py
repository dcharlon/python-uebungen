names = []
while True:
    try:
        name = input("name: ").title()
        names.append(name)
    except EOFError:
        break
if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif len(names) > 2:
    new_names = ", ".join(names[0:-1])
    print(f"Adieu, adieu, to {new_names}, and {names[-1]}")
else:
    print("You did not enter a name! ")