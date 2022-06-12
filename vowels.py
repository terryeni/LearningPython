vowels = ["a", "e", "i", "o", "u"]
word = input("Provide a  word to search for vowels: ")
found = []
for latter in word:
    if latter in vowels:
        if latter not in found:
            found.append(latter)
for vowels in found:
    print(vowels)
