from Menu import menu

orders = []


def add_order():
    name = input("Product name: ").strip().lower()
    if name not in menu:
        print("This product is not on the menu!")
        return
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Quantity must be a whole number!")
        return
    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return
    orders.append({"name": name, "price": menu[name], "quantity": quantity})
    print(f"{quantity} x {name} added to your order.")


def show_orders():
    if len(orders) == 0:
        print("No orders yet.")
        return
    print("\n------ Orders ------")
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order['name']} | Price: {order['price']:,} | Quantity: {order['quantity']}")
