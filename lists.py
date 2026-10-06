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

#table of 7
multiples = [i * 7 for i in range(1, 11)]
print(multiples)  # Output: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]