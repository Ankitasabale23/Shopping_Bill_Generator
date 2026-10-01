# Shopping Bill Generator
def calculate_discount(subtotal, discount_rate):
    return subtotal * discount_rate / 100
def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100
print("===== SHOPPING BILL GENERATOR =====")
products = []
number_of_products = int(input("Enter number of products: "))
for i in range(number_of_products):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    total = quantity * price
    products.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "total": total
    })
subtotal = sum(product["total"] for product in products)
discount_rate = float(input("\nEnter discount percentage: "))
discount = calculate_discount(subtotal, discount_rate)
amount_after_discount = subtotal - discount
tax_rate = float(input("Enter tax percentage: "))
tax = calculate_tax(amount_after_discount, tax_rate)
final_amount = amount_after_discount + tax
print("\n========== SHOPPING BILL ==========")
print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
print("-" * 43)
for product in products:
    print(
        f"{product['name']:<15}"
        f"{product['quantity']:<8}"
        f"{product['price']:<10.2f}"
        f"{product['total']:<10.2f}"
    )
print("-" * 43)
print(f"Subtotal:             ₹{subtotal:.2f}")
print(f"Discount ({discount_rate:.1f}%):     -₹{discount:.2f}")
print(f"Tax ({tax_rate:.1f}%):          ₹{tax:.2f}")
print(f"Final Amount:         ₹{final_amount:.2f}")
print("===================================")