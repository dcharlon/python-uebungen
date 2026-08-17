s = input("Give me some text: ")
result = ""
vocals = ["a", "e", "i", "o", "u"]
for c in s:
    if c.casefold() not in vocals:
        result += c
print(result)