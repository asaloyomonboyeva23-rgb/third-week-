
age = int(input("enter your age :"))
print("---movie tivket pricer ---" "\n")

if age <= 12 :
    price = 8 
    print("you fall into the 'children' category.")
elif age <65 :
    price = 15
    print("you fall into the 'adult' category.")
else  :
    price = 10
    print("you fall into the 'seniour' category.")
print(f" your admission price is {price}")
 
 