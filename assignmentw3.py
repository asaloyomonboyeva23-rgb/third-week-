print("== Museum Admission Calculator ===")
print("Enter exhibit type: general, special, or vip , Type 'done' when finished selecting exhibits")
total_cost = 0.0
while True :
    exhibit_type = input("Enter exhibit type: ")
    if exhibit_type == "done" :
        break
    elif exhibit_type == "general":
        price = 9.00
        print (f"exhibit_type :{price} ")
    elif exhibit_type == "special":
        price = 14.00
        print (f"exhibit_type :{price} ")
    elif exhibit_type == "vip":
        price = 20.00
        print (f"exhibit_type :{price} ")
    total_cost+=(price)
    print(f"current total : {total_cost}")
if total_cost >= 55.00:
    discount = 8
    final_cost = total_cost - discount 
else :
    final_cost = total_cost
print("=== Admission Summary ===")
print(f"Subtotal: {final_cost}")
print(f"Group Visit Discount: { '-8' if total_cost >=55 else 'no discount'} ")
print(f"Final Total: {final_cost}")
print("Thank you for visiting!")
