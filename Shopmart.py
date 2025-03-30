print("Welcome to the ShopMart online cart \n")
print("******************************************************************************************************************** \n")
avilable_items= ["apple", "banana", "milk", "egg", "mango", "spinach", "orange", "ice cream", "pizza", "french fries"] or ["apples", "bannas", "milks", "eggs", "mangoes", "spinaches", "oranges", "french fries","pizzas", "ice creams" ]
prices=[1.25, 1.46, 3.77, 4.99, 3.99, 1.28, 4.33, 5.00, 7.66, 4.68 ]
cart=[] 
Bill=0.00
while True:
    print(f"Items available are{avilable_items} \n")
    Wanted_Item=input("What item would you like").lower()
    if Wanted_Item in avilable_items:
        idx= avilable_items.index(Wanted_Item)
        print(f"That would be {prices[idx]}")
        
        cart.append(Wanted_Item) 
        Bill += prices[idx]
    else:
        print("The item you've put does not exist")
    Choice= input("Would you like to remove any items Y/N").lower()
    if Choice =="y":
        Remove_item=input("Which item would you like to remove")
        idx= avilable_items.index(Remove_item)
        Bill -= prices[idx]
        cart.remove(Wanted_Item)
    elif "n":
        print("This item will remain in your cart")
    print(f"The current items in your cart are {cart}")
    Done=input("Is this all you would like in the cart Y/N").lower()
    if Done == 'y':
     print(f"The items you've bought are {cart}")
     print(f"The total cost is{Bill}")
     break

        