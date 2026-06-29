def calculate_total_cost(cart):
    total_cost = 0 

    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

cart = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 4}, 
    {'name': 'Banana', 'price': 0.3, 'quantity': 6},
    {'name': 'Orange', 'price': 0.8, 'quantity': 3}
    ] 

print(calculate_total_cost(cart)) 