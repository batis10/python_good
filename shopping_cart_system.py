products = []


while True:
  choice = int(input("1 : Add \n2: Remove \n3 : List All Items \n4 :Total price \n"))

  if choice == 1:
    name = input("enter product name: ")
    price = float(input("enter product price: "))
    quantity = int(input("enter quantity: "))
    item = {"name": name, "price":price, "quantity": quantity}
    products.append(item)
    
    print("product added !!!!")

  
  elif choice ==2:
    #remove
    name = input("enter product name to remove: ")
    for item in products:
      if name in item:
        products.remove(item)
        print("product deleted")
    else:
      print("item not found")    

    pass
  
  elif choice ==3:
    for item in products:
      print(f"Name:{item["name"]} Quantity: {item["quantity"]} Price: {item["price"]} Total: {item["price"]*item["price"]}" )
    pass
  
  elif choice ==4:
    total_price=0.0
    for item in products:
      item_total_price= item["price"]*item["quantity"]
      total=total_price + item_total_price
    pass
  print("your total is : {total}")
  
else:
  print("invalid ")


  
  
  
  
