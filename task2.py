print("--- running total calcuator ---")
total =0
while True :
    user_input = input("enter numbers to add or type 'done' to see the total")
    if user_input == ("done") :
        break
    total += float(user_input)
    print(total)
print(f"The final sum of all numbers is : {total}")
