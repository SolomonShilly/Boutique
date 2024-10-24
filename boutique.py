inventory = {
    "Jeans": {"price": 50, "stock": 5},
    "TShirt": {"price": 25, "stock": 10},
    "Hoodie": {"price": 60, "stock": 7}
}

salesTotal = 0

def show_inventory():
  print("Available Products: ")
  for item, details in inventory.items():
    print(f"{item} - ${details['price']} (Stock:{details['stock']})")

def take_order():
  global salesTotal
  customer = input("Enter customer name: ")
  show_inventory()
  orderItem = input("what would you like to buy? ").title()

  if orderItem in inventory and inventory[orderItem]["stock"] > 0:
    print(f"{orderItem} added to cart for ${inventory[orderItem]['price']}")
    inventory[orderItem]["stock"] -= 1
    salesTotal += inventory[orderItem]["price"]

    with open("orders.txt", "a") as file:
      file.write(f"{customer} brought {orderItem} for ${inventory[orderItem]['price']}\n")
  else:
    print(f"Sorry, {orderItem} is out of stock or not available.")

# "r" is to read, "w" to write, "a" to append
def view_sales():
  print(f"\nTotal Sales: ${salesTotal}")
  print("Orders so far:")
  try:
    with open("orders.txt", "r") as file:
      print(file.read())
  except FileNotFoundError:
      print("No sales recorded yet.")

while True:
  print("\nWelcome to Macys!")
  action = input("Would you like to 'order', 'view sales', or 'exit'?").lower()

  if action == "order":
      take_order()
  elif action == "view sales":
      view_sales()
  elif action == "exit":
      print("Thank you for visiting Macys!")
  else:
    print(f"Excuse Me! You can not {action} here! This is a Macys.")