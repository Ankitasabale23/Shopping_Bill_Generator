# Shopping Bill Generator

## 1. Objective

The objective of this task is to create a Python program that accepts product names, quantities, and prices and generates a formatted shopping bill with subtotal, discount, tax, and final amount.

## 2. Tools Used

- Python
- Visual Studio Code
- GitHub

## 3. Programming Language

Python

## 4. Description

The Shopping Bill Generator is a simple Python program that calculates the total cost of products purchased by a customer.

The program accepts product details such as product name, quantity, and price. It calculates the total price for each product and generates an itemized bill.

The program also calculates discount, tax, and the final amount to be paid.

## 5. Features

- Accept multiple products
- Store product details
- Calculate total price for each product
- Calculate subtotal
- Apply discount
- Calculate tax
- Calculate final amount
- Display a formatted itemized bill
- Display monetary values up to two decimal places

## 6. Working of the Program

1. The program asks the user for the number of products.
2. Product name, quantity, and price are entered for each product.
3. The total price of each product is calculated.
4. Product details are stored using a dictionary.
5. The subtotal is calculated by adding all product totals.
6. The discount percentage is entered and the discount amount is calculated.
7. Tax is calculated on the amount after discount.
8. The final amount is calculated by adding the tax.
9. The complete shopping bill is displayed.

## 7. Calculations

### Product Total

Product Total = Quantity × Price

### Subtotal

Subtotal = Sum of all Product Totals

### Discount

Discount = Subtotal × Discount Rate / 100

### Amount After Discount

Amount After Discount = Subtotal - Discount

### Tax

Tax = Amount After Discount × Tax Rate / 100

### Final Amount

Final Amount = Amount After Discount + Tax

## 8. Sample Execution

```text
===== SHOPPING BILL GENERATOR =====
Enter number of products: 2

Product 1
Enter product name: Pen
Enter quantity: 2
Enter price per item: 20

Product 2
Enter product name: Notebook
Enter quantity: 3
Enter price per item: 50

Enter discount percentage: 10
Enter tax percentage: 5

========== SHOPPING BILL ==========
Product        Qty     Price     Total
-------------------------------------------
Pen            2       20.00     40.00
Notebook       3       50.00     150.00
-------------------------------------------
Subtotal:             ₹190.00
Discount (10.0%):     -₹19.00
Tax (5.0%):           ₹8.55
Final Amount:         ₹179.55
===================================