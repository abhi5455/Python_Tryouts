name1 = input("Enter the name of 1st person: ")
dob1 = input("Enter DOB of 1st person(DD/MM/YYYY): ")
dob1_d, dob1_m, dob1_y = int(dob1[:2]), int(dob1[3:5]), int(dob1[6:])

name2 = input("Enter the name of 2nd person: ")
dob2 = input("Enter DOB of 2nd person(DD/MM/YYYY): ")
dob2_d, dob2_m, dob2_y = int(dob2[:2]), int(dob2[3:5]), int(dob2[6:])

younger = ""
if dob1_y > dob2_y:
    younger = name1
elif dob1_y < dob2_y:
    younger = name2
else:
    if dob1_m > dob2_m:
        younger = name1
    elif dob1_m < dob2_m:
        younger = name2
    else:
        if dob1_d > dob2_d:
            younger = name1
        elif dob1_d < dob2_d:
            younger = name2
        else:
            # case where both born on same day
            if name1>name2:
                younger = name2
            else:
                younger = name1
print("Younger Person is:", younger)
