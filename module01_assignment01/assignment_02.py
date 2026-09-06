print('\n==Welcome to your shopping cart==\n')

name = input("Enter your name: ")

product_1 = input("Enter the name of 1st product: ")
product_1_price = float(input("Enter 1st product's price: "))

product_2 = input("Enter the name of 2nd product: ")
product_2_price = float(input("Enter 2nd product's price: "))

product_3 = input("Enter the name of 3rd product: ")
product_3_price = float(input("Enter 3rd product's price: "))

subtotal = product_1_price + product_2_price + product_3_price

discount = 0.0

if subtotal >= 5000:
    discount = 20
elif 4999 >= subtotal >= 3000:
    discount = 10
elif 2999 >= subtotal >= 1000:
    discount = 5
elif subtotal < 1000:
    discount = 0
else:
    discount = 0
    
discount = discount/100

actual_discount = subtotal * discount

final_total = subtotal - actual_discount

print(f"\n\nCustomer Name: {name}\n\nProduct 1: {product_1}\nPrice: {product_1_price:.2f}\n\nProduct 2: {product_2}\nPrice: {product_2_price:.2f}\n\nProduct 3:{product_3}\nPrice: {product_3_price:.2f}\n\nSubtotal: {subtotal:.2f}\nDiscount: {actual_discount:.2f}\nFinal Total: {final_total:.2f}\n\n")


