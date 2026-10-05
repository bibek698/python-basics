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
