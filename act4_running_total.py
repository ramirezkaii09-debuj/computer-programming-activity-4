# Activity 2: Running Total
# Read item prices until the user enters 0 (sentinel).
# Print the number of items, the total, and the average price to 2 decimals.

total = 0.0
count = 0

while True:
    try:
        price = float(input("Price (0 to stop): "))
        if price == 0:
            break
        total += price
        count += 1
    except ValueError:
        pass

if count > 0:
    average = total / count
else:
    average = 0.0

# Print results with formatting
print(f"Items: {count}  Total: {total:.2f}")
print(f"Average: {average:.2f}")
