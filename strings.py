text = "Random string with a lot of characters"
print(text[-1]) #prints"s"
print(text[-2]) #prints"r"

color = "Orange"
color[1:4] #prints "ran"

fruit = "Pineapple"
print(fruit[:4]) #prints "Pine"
print(fruit[4:]) #prints "apple"

message = "A kong string with silly typo"
new_message = message[0:2] + "l" + message[3:] #replaces "kong" with "long"
print(new_message) #prints "A long string with silly typo"

"...".join(["This", "is", "a", "sentence", "joined", "with", "dots"]) #prints "This...is...a...sentence...joined...with...dots"

name = "Bibek"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number)) #prints "Hello Bibek, your lucky number is 15"