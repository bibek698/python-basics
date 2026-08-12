def greeting(name,department):
    print("Hello," + name + "!")
    print("You are part of " + department + " department.")

greeting("Bibek", "Engineering")

greeting("Biraj", "Marketing")

#built-in functions

#type()
print(type("This is a string"))
#str()
number = 12
string_representation = str(number)
print(string_representation)
#sorted()
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)
#min() & max()
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Bibek")
lucky_number("Raj")