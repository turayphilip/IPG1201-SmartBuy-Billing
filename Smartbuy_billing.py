
print("=" * 50)
print(" WELCOME TO SMARTBUY SUPERMARKET")
print(" BILLING SYSTEM")
print("=" * 50)

process_next_customer = "Y" # Variable - String data type

# Loop for multiple customers - Concept 5: Loops
while process_next_customer.upper() == "Y":
    
    # Variables & Data Types - Concept 1
    total_bill = 0.0 # Float data type
    product_names = [] # Array/List - Concept 6
    quantities = [] # Array/List - Concept 6
    prices = [] # Array/List - Concept 6
    
    add_product = "Y"
    
    # Loop for multiple products per customer - Concept 5: Loops
    while add_product.upper() == "Y":
        
        # Input statements - Concept 2
        product_name = input("\nEnter product name: ") # String
        quantity = int(input("Enter quantity: ")) # Integer
        price = float(input("Enter price per item: Le ")) # Float
        
        # Arithmetic operators - Concept 3
        amount = quantity * price # Multiplication
        total_bill = total_bill + amount # Addition
        
        # Store in lists/arrays - Concept 6
        product_names.append(product_name)
        quantities.append(quantity)
        prices.append(price)
        
        print(f"Added: {product_name} | Amount: Le {amount:.2f}")
        
        # Input statement - Concept 2
        add_product = input("\nAdd another product? Y/N: ")
    
    # Decision structure - Concept 4: if-else
    if total_bill > 500: # Promotional discount condition
        discount = total_bill * 0.10 # Arithmetic - Concept 3
        final_bill = total_bill - discount # Arithmetic - Concept 3
        print(f"\nCongratulations! You get 10% discount.")
    else:
        discount = 0.0
        final_bill = total_bill
    
    # Output statements - Concept 2: Display receipt
    print("\n" + "=" * 50)
    print(" SMARTBUY SUPERMARKET RECEIPT")
    print("=" * 50)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<10} {'Amount':<10}")
    print("-" * 50)
    
    # Loop through arrays to print items - Concept 5 & 6
    for i in range(len(product_names)):
        item_total = quantities[i] * prices[i] # Arithmetic - Concept 3
        print(f"{product_names[i]:<15} {quantities[i]:<5} Le {prices[i]:<8.2f} Le {item_total:.2f}")
    
    print("-" * 50)
    print(f"{'Subtotal:':<32} Le {total_bill:.2f}")
    print(f"{'Discount 10%:':<32} Le {discount:.2f}")
    print(f"{'FINAL TOTAL:':<32} Le {final_bill:.2f}")
    print("=" * 50)
    print(" Thank you for shopping with SmartBuy!")
    print("=" * 50)
    
    # Input for next customer - Concept 2
    process_next_customer = input("\nProcess next customer? Y/N: ")

print("\nSystem shutdown. Goodbye!")
