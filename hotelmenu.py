#define the menu of the cafe
menu = {
    'coffee': 80,
    'pasta': 120,
    'burger':100,
    'sandwich': 80,
    'pizza':100,
}
# greet
print("Welcome to PYTHON CAFE")
print("cofee: RS80\n pasta: RS120\n burger: RS100\n sandwich: RS80\n pizza: RS100")


order_total = 0
  
item_1 = input("enter the name of the item you want to order = ") 
if item_1 in menu :
    order_total += menu[item_1] #0+80
    print(f"ordered item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet !")   

another_order = input("DO you want to add another item ? (yes/no )") 
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available !")    
print(f"The Total amount of item to pay is {order_total}")        
