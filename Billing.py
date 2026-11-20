from Order import orders


def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total


def calculate_discount(total):
    if total > 1000000:
        return total * 10 / 100
    return 0


def print_invoice():
    if len(orders) == 0:
        print("No orders to invoice.")
        return
    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount
    print("\n========== Invoice ==========")
    for order in orders:
        print(f"{order['name']:<10} x {order['quantity']}")
    print("-----------------------------")
    print(f"Total      : {total:,.0f} Toman")
    print(f"Discount   : {discount:,.0f} Toman")
    print(f"Final price: {final_price:,.0f} Toman")
    print("=============================")
