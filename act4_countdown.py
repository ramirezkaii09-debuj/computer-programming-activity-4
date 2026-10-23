# Activity 1: Countdown Timer
# Read a whole number n. Keep asking while n is not positive.
# Then count down from n to 1 on one line and finish with "Liftoff!".

while True:
    try:
        n = int(input("Enter n: "))
        if n > 0:
            break
    except ValueError:
        pass

# Count down from n to 1
current = n
output_str = ""
while current >= 1:
    output_str += str(current) + " "
    current -= 1

output_str += "Liftoff!"
print(output_str)
