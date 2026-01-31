# A tracker for student.




print("Welcome to the Daily Study Tracker!")

name = input("Enter your name: ")
subject1 = input("Enter your first subject: ")
subject2 = input("Enter your second subject: ")
subject3 = input("Enter your third subject: ")

hours1 = float(input(f"How many hours did you study {subject1} today? "))
hours2 = float(input(f"How many hours did you study {subject2} today? "))
hours3 = float(input(f"How many hours did you study {subject3} today? "))

total_hours = hours1 + hours2 + hours3
average_hours = total_hours / 3


if total_hours >= 6:
    feedback = "Great job! You studied a lot today."
elif total_hours >= 3:
    feedback = "Good effort! Try to study a bit more tomorrow."
else:
    feedback = "You should study more. Keep going!"


if hours1 >= hours2 and hours1 >= hours3:
    best_subject = subject1
elif hours2 >= hours3:
    best_subject = subject2
else:
    best_subject = subject3

print("\n" + "-" * 30)
print("     DAILY STUDY REPORT")
print("-" * 30)
print(f"Student: {name}")
print(f"{subject1}: {hours1} hours")
print(f"{subject2}: {hours2} hours")
print(f"{subject3}: {hours3} hours")
print(f"Total study time: {total_hours} hours")
print(f"Average per subject: {average_hours:.2f} hours")
print(f"Best subject today: {best_subject}")
print(feedback)
print("-" * 30)