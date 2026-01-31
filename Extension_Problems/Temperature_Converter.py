choice = input("Convert C to F or F to C? (Enter C or F): ").upper()
temp = float(input("Enter the temperature: "))

if choice == "C":
    result = (temp * 9/5) + 32
    print(result)
elif choice == "F":
    result = (temp - 32) * 5/9
    print(result)