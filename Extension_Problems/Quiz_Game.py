score = 0

ans1 = input("What is the capital of France? ").strip().lower()
if ans1 == "paris":
    score += 1

ans2 = input("What is 5 + 7? ").strip()
if ans2 == "12":
    score += 1

ans3 = input("Which planet is known as the Red Planet? ").strip().lower()
if ans3 == "mars":
    score += 1

print(score)

if score == 3:
    print("Perfect! Excellent!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep practicing!")
else:
    print("Study more!")