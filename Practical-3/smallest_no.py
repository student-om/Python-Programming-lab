smallest = None
for value in [33, 244, 7, 3, 4]:
    if smallest is None:
        smallest = value

    elif smallest > value:
        smallest = value

print(smallest)

for letter in 'banana':
    print(letter)

count = 0
for letter in 'banana':
    if letter == 'a':
        count += 1

print(count)