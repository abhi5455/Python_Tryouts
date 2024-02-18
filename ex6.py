Str = input("Enter a String (Only Alphabets): ")
Str1 = ""
for char in Str:
    if 'A' <= char <= 'Z':
        Str1 += chr(ord(char)+32)
    else:
        Str1 += char
Str2 = "abcdefghijklmnopqrstuvxyz "
Str3 = ""
for char in Str2:
    for char1 in Str1:
        if char == char1:
            Str3 += char1
print("Lower Case: ", Str1)
print("Sorted String: ", Str3)
