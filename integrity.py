s = input("Enter string: ")

if s == s[::-1]:
    print("Valid")
else:
    print("Corrupted")