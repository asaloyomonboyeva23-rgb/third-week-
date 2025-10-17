print("== Pet Grooming Service Calculator ===")
print("Enter service package: bath, trim, or full , Type 'done' when finished selecting services")
total_cost = 0.0

while True :
    user_input = input("Enter service package: ")
    if user_input == "done":
        break
    elif user_input == "bath":
        price = 15
        print(f"price: {price}")
    elif user_input == "trim":
        price = 25
        print(f"price:{price}")
    elif user_input == "full":
        price = 40
        print(f"price: {price}")
    total_cost += (price)
    print(f"Current total: ${total_cost}")
if total_cost >= 75:
    discount = int(12)
    final_cost = total_cost - discount
else : 
    final_cost = total_cost 
print(f"Final total: ${final_cost}")
print("=== Service Summary ===")
print(f"Subtotal: {total_cost}")
print(f"Multi-Pet Discount : { '-12 ' if  total_cost >= 75  else 'no discount'}")
print(f"Final Total:{final_cost }")
print("Thank you for choosing our salon!")