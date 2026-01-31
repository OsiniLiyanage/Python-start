password = input("Enter your password: ")
length = len(password)

if length < 6:
    print("Weak password")
elif 6 <= length <= 10:
    print("Medium password")
else:
    print("Strong password")