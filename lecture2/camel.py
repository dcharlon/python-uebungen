s = input("Give me a name in camel case: ")
result = ""
for c in s:
    if c.islower():
        result += c
    else:
        result += "_"
        result += c.casefold()
print(result)


