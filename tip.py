print("Hello welcome to tip calculator")
print("tell about your bill")

n = int(input("Total items you got : "))

items = []
prices = []
#Bill calculation
for i in range(n):
    item = input(f"Enter name of yor item {i + 1}:")
    price = float(input(f"Enter the price for item {i + 1}:"))
    items.append(item)
    prices.append(price)

total = sum(prices)
#Bill before tip display
print("\n-- Bill_Summary---")

for i in range(n):
    print(f"Item{i+1}: {items[i]} - ₹{prices[i]}")

    print(f"\nTotal Bill: ₹{total:.2f}")
#tip choice
tip_choice = input("do you wanna tip Y or N : ")

if tip_choice == "Y":
    tip_amount = float(input(f"how much do you wanna tip (your current bill is {total:.2f} ) .... please tip some hehe" ))
    final_total = total + tip_amount
    print(f"Tip Amount: ₹{tip_amount:.2f}")
    print(f"Final Total (with tip): ₹{final_total:.2f}")

else:
    tip_amount = 0
    final_total = total
    print(f"Final Total : ₹{final_total:.2f}")
