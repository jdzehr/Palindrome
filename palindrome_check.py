string1 = input("Enter a word: ")
print(string1)
string1 = string1.lower()
print("Reversing the word...")

if string1[::-1] == string1:
    print(string1[::1])
    print("The word is a Palindrome!")
else:
    print("This word/string is not a Palindrome :(")