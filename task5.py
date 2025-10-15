print("-- Fibonacci Sequence Generator ---")
user_input = int(input("How many Fibonacci numbers would you like to generate? "))
a= 0
b=1

print(a)

for i in range(user_input):
    print(a,end=" ")
    a,b=b,a+b
    
