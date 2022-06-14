phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

for i in range(4):
    plist.pop()

# pop the object at the location 0 which is the first letter in the list
plist.pop(0)

# find and remove " ' "
plist.remove("'")

# This line of code pops the space from the list,
# then inserts it back into the list at index location 2.
# the pop occurs first before the insert happens.
plist.extend([plist.pop(), plist.pop()])


plist.insert(2, plist.pop(3))

print(phrase)
print(plist)
