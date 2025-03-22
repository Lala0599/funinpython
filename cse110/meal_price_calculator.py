#meal price calculator. Total price of a meal, incl sales tax, a tip, 
# and change after payment. In addition, the ability to add a tip % to the
#total bill.

#function to format currency values

def format_currency(amount):
    return f"${amount:.2f}"

#ask for prices

child_meal_price = float(input("\nWhat is the price of a child's meal? : "))
adult_meal_price = float(input("\nWhat is the price of a adult's meal? : "))

#prompt number of children and adults

num_children = int(input("\nHow many children ordered food? :"))
num_adults = int(input("\nHow many adults ordered food? :"))

#subtotal

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"\nSubtotal: {format_currency(subtotal)}")

#tax rate

sales_tax_rate = float(input("\nWhat is the sales tax rate? :"))

#actual tax
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: {format_currency(sales_tax)}")

#total price

total = subtotal + sales_tax
print(f"Total: {format_currency(total)}")

#ask if user wants to add a tip

add_tip = input("\nWould you like to add a tip? (yes/no)").strip().lower()
if add_tip == "yes":
    tip_percentage = float(input("\nWhat percentage would you like to tip? : "))
    tip_amount = total * (tip_percentage / 100)
    total += tip_amount
    print(f"Tip Amount: {format_currency(tip_amount)}")
    print(f"New Total (including tip): {format_currency(total)}")

#prompt for payment amount
payment_amount = float(input("\nWhat is the payment amount? : "))

#change
change = payment_amount - total
print(f"Change: {format_currency(change)}")