n = int(input("Enter How Many Numbers: "))
print("Enter {n} numbers".format(n=n))
Num = []
i = 0
while i < n:
    x = 1
    Str = input()
    if Str.count(" ") != 0:
        # Handles the case when Numbers are entered by separating spaces
        parts = Str.split(" ")
        for part in parts:
            if i == n:
                break
            Num.append(int(part))
            i = i+1
    else:
        # Handles the case when Numbers are entered line by line
        Num.append(int(Str))
        i = i+1
print("List:", Num)
print("Extracting from list")
start = int(input("Enter Start Index:"))
End = int(input("Enter End Index:"))
if End >= n:
    print("End Index exceeds size\nPrinting from startIndex to End of list")
    End = len(Num)-1
# Slicing
print(Num[start:End+1])
