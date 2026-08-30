for x in range(5):
    print(x)

friends = ["John", "Bibek", "Sita", "Ram"]
for friend in friends:
    print("Hello " + friend)

#finding sum and average of numbers in a list

number = [1, 2, 3, 4, 5]
sum = 0
length = 0
for num in number:
    sum += num
    length += 1
print("Sum:", str(sum))
print("Average:", str(sum / length))