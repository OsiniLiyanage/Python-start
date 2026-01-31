age = int(input("Enter your age: "))

if 0 <= age <= 12:
    category = "Child"
    price = 8
elif 13 <= age <= 17:
    category = "Teen"
    price = 10
elif 18 <= age <= 64:
    category = "Adult"
    price = 15
else:
    category = "Senior"
    price = 10

print(category)
print(price)