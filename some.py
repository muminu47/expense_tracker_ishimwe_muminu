expense_name=input("enter item_name: ")
expense_amount= int(input("enter item_amount: "))
category=""
if expense_amount>=3000:
    category = "food"
elif expense_amount>=10000:
    category = "transport"  
elif expense_amount>=20000:
    category = "entertaiment" 
else :
    category = "major expense" 
print ("the product is" , expense_name)
print ("the amount ", expense_amount)
print ("the category is", category)