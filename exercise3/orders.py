import json

with open('data/orders.json','r') as file:
    orders_data = json.load(file)

for order in orders_data:
    print(f"Order id: {order['order_id']}")
    print(f"Customer: {order['customer']}")
    print(f"Order date:{order['order_date']}")
    print(f"Status: {order['status']}")
    print("Products:")
    
    total_price = 0
    
    for products in order['products']:
        name= products['name']
        quantity = products['quantity']
        price = products['price']
        product_total = price*quantity
        total_price += product_total
        
        print(f"Product: {name:<20} Quantity: {quantity:<4} Price: {price:<8} Total price: {product_total:.2f}")
        
    print(f"Total price :{total_price:.2f}")
    print("\n" + "-"*40 + "\n")