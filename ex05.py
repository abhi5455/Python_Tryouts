Str = input("Enter a String: ")
Len = len(Str)
Str1 = ""
Str2 = ""
for char in Str:
    if 'A' <= char <= 'Z':
        Str1 += chr(ord(char) + 32)
        Str2 += char
    else:
        Str1 += char
        if 'a' <= char <= 'z':
            Str2 += chr(ord(char) - 32)
        else:
            Str2 += char
print("Original String: ", Str)
print("Upper Case: ", Str2)
print("Lower Case: ", Str1)
