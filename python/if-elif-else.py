# TAKING INPUT FROM USER AND USING IF-ELIF AND ELSE STATEMENT

age = int(input("Enter your age : "))

if age >= 18 :                  # if this statement then 

    print("You're an adult")
    print("You're elligible for voting")
    
elif age < 18 and age > 3 :     # if if statement is false then
    print("You're in school")

else :
    print("You're a kid")       # if both if and elif statement is false
    
print("Thank You !!")