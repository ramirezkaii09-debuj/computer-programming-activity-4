# Activity 3: PIN Lock
# The correct PIN is "1234". Give the user at most 3 tries.
# Print "Access granted" on a match, or "Card blocked" after 3 wrong tries.

CORRECT_PIN = "1234"
attempts = 0
max_attempts = 3
granted = False

while attempts < max_attempts:
    pin = input("PIN: ")
    attempts += 1
    if pin == CORRECT_PIN:
        granted = True
        break

if granted:
    print("Access granted")
else:
    print("Card blocked")
