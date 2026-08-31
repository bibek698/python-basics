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

#if we do not want to start for loop with 0 we use

product = 1
for n in range(1,10):
  product = product * n

print(product)

#if we want to increase the value of n by 10 we use
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

for element in long_list:
  do_something(element)

for element1 in long_list:
  for element2 in long_list:
    do_something(element1, element2)