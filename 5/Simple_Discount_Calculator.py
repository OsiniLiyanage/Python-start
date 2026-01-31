purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 100:
    discount_rate = 0.20
elif purchase_amount >= 50:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print(purchase_amount)
print(discount_amount)
print(final_price)