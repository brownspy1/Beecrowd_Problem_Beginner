# Snack
""" Using the following table, write a program that reads
a code and the amount of an item. After, print the value to pay.
This is a very simple program with the only
intention of practice of selection commands."""

code, qun = list(map(int, input().split()))

if code == 1:
    price = 4.00
    fin = price * qun
    print(f'Total: R$ {fin:.2f}')
elif code == 2:
    price = 4.50
    fin = price * qun
    print(f'Total: R$ {fin:.2f}')
elif code == 3:
    price = 5.00
    fin = price * qun
    print(f'Total: R$ {fin:.2f}')
elif code == 4:
    price = 2.00
    fin = price * qun
    print(f'Total: R$ {fin:.2f}')
elif code == 5:
    price = 1.50
    fin = price * qun
    print(f'Total: R$ {fin:.2f}')

'''short mathod'''
code, qun = list(map(int, input().split()))

# Create a dictionary of prices
prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

# Calculate the total price
fin = prices[code] * qun

# Print the total price
print(f'Total: R$ {fin:.2f}')
