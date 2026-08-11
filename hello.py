print("hello world")

print(7+8.5) #implicit conversion: converting one data type to another data type (automatic conversion)
print("a"+"b"+"c")
print("This " + "is " + "pretty " + "neat!")

base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) #explicit conversion: converted integer to string (manual converesion)

#type annotation of variables

import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}