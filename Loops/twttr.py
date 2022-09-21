text = input("Input: ")
print("Output: ",end="")
for letter in text:
    if not letter.lower() in ['a','i','o','u','e']:
        print(letter,end="")
print()
