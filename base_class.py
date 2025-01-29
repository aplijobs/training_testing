from typing import List

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

class ShoppingCart:
    def __init__(self, client_name: str):
        self.client_name = client_name
        self.items: List[dict] = []
        self.total: float = 0.0

    def add_product(self, product: Product, quantity: int):
        for item in self.items:
            if item['product'].name == product.name:
                item['quantity'] += quantity
                self.total += product.price * quantity
                return
        self.items.append({'product': product, 'quantity': quantity})
        self.total += product.price * quantity

    def remove_product(self, product_name: str, quantity: int = 1):
        for item in self.items:
            if item['product'].name == product_name:
                if item['quantity'] <= quantity:
                    self.total -= item['product'].price * item['quantity']
                    self.items.remove(item)
                else:
                    item['quantity'] -= quantity
                    self.total -= item['product'].price * quantity
                return
        raise ValueError(f"Product '{product_name}' not found in the cart")

    def clear_cart(self):
        self.items.clear()
        self.total = 0.0

    def checkout(self):
        if not self.items:
            raise ValueError("Cannot checkout an empty cart")

        receipt = f"Receipt for {self.client_name}:\n"
        receipt += "\n".join([f"- {item['product'].name} (x{item['quantity']}): ${item['product'].price * item['quantity']:.2f}" for item in self.items])
        receipt += f"\nTotal: ${self.total:.2f}"

        self.clear_cart()
        return receipt

    def __repr__(self):
        return f"ShoppingCart(client_name={self.client_name}, items={self.items}, total={self.total:.2f})"

# Example Usage
if __name__ == "__main__":
    cart = ShoppingCart("John Doe")
    cart.add_product(Product("Apple", 1.2), 3)
    cart.add_product(Product("Banana", 0.5), 5)
    print(cart)

    cart.remove_product("Apple", 2)
    print(cart)

    print(cart.checkout())
    print(cart)
