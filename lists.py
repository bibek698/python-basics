x = ['we', 'are', 'learning', 'Python', 'programming']
print(x[0])  # Output: we
print(x[1:3])  # Output: ['are', 'learning']
'are' in x  # Output: True
'not' in x  # Output: False
print(len(x))  # Output: 5
print(x[:2])  # Output: ['we', 'are']
print(x[2:])  # Output: ['learning', 'Python', 'programming']


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")

fruits.insert(0, "Orange")
print(fruits)
fruits.remove("Melon")


#iterating through a list
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

#table of 7
multiples = []
for i in range(1, 11):
  multiples.append(i * 7)
print(multiples)  # Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#table of 7 using list comprehension
multiples = [i * 7 for i in range(1, 11)]
print(multiples)  # Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#for loop vs list comprehension
### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

# Select Run to compare the two results.