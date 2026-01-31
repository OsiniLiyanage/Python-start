name = input("Enter student name: ")
maths = float(input("Enter score for Maths: "))
science = float(input("Enter score for Science: "))
history = float(input("Enter score for History: "))

average = (maths + science + history) / 3

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

status = "Pass" if average >= 60 else "Fail"

print("\n" + "="*30)
print("        REPORT CARD")
print("="*30)
print(f"Student Name: {name}")
print("-"*30)
print(f"Maths    : {maths:.2f}")
print(f"Science  : {science:.2f}")
print(f"History  : {history:.2f}")
print("-"*30)
print(f"Average  : {average:.2f}")
print(f"Grade    : {letter_grade}")
print(f"Status   : {status}")
print("="*30)