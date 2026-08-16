x, y, z = input("Give me a simple arithmetic expression: ").split(" ")

if y == "+":
    print(f"{int(x) + int(z):.1f}") 

elif y == "/":
    print(f"{int(x) / int(z):.1f}")

elif y == "*":
    print(f"{int(x) * int(z):.1f}") 

elif y == "-":
    print(f"{int(x) - int(z):.1f}") 

    
    
    