marks = []
n = int(input("Enter the number of students: "))
print("Enter", n, "Marks")
for i in range(n):
    marks.append(float(input()))
i = 0
# Sorting
while i < len(marks):
    j = 0
    while j < (len(marks)-i-1):
        if marks[j] > marks[j+1]:
            temp = marks[j]
            marks[j] = marks[j+1]
            marks[j+1] = temp
        j = j+1
    i = i+1
print("Entered Marks are:", end=" ")
average=0.0
for i in marks:
    print(i, end="  ")
    average += i
print("\nAverage:", average/len(marks))
print("Median:", end=" ")
if len(marks) % 2 != 0:
    print(marks[len(marks)//2])
else:
    middle = len(marks)//2
    print((marks[middle] + marks[middle-1])/2)
