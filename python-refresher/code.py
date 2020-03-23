### F string

name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

#### format template

greeting = "Hello, {}. Today is {}"
with_name = greeting.format("Bob", "Monday")

print(with_name)

square_feet = 500
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} sqaure metres.") ## .2f to round the number 

### tuple

single_value_tuple = 15, # or (15, )

### advanced set operations

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) ## it removes the items in abroad from friends
print(f"local: {local_friends}")
print(f"Common: {friends.intersection(abroad)}") ## it gets the elements in commmon

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(f"friends: {friends}")

### comparation

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad) ## compares values
print(friends is abroad) ## compare memory address

### String
print("LOWER-CASE".lower())