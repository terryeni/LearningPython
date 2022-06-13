'''declare a variable called "phrase" 
and assigne "don't panic" to the variable. 
convert the object of the variable to a list in a new variable '''

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

'''Change the object of the phrase variable to "on tap" 
using the method avaible with the list function. use the for loop to '''
for i in range(4):
    plist.pop()

plist.pop(0)
plist.insert(4, "a")
plist.remove("'")
plist.remove(" ")
plist.insert(2, " ")
plist.pop()

''' could potentially use the pop method to remove the last object in the variable. 
however, i have used the for loop as that's more effiecient and clean code
plist.pop()
plist.pop()
plist.pop()
plist.pop()
'''
print(plist)
