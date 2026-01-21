## Python is case sensitive i.e "a" and "A" are not same. both are different 
environment = input("Enter Environment name:")
##environment = "PrcoD"
change_ticket = False
print((type(environment)))
environment = environment.casefold()
print(environment)

if environment == "prod":
   change_ticket = True
   print("please provide change request")

elif environment == "preprod":
     print("Welcome to Preprod Environment")

else:
     print("please login with yours credentails")