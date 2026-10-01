string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”


# Prints “Hello world”
print("Hello" + " " + "world")

greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')