class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        return sum(p.price * p.quantity for p in self.products)

     # Dodaj metod u ProductManager (product_manager.py)
    def remove_product(self, name: str) -> bool:
        for i, p in enumerate(self.products):
            if p.name.lower() == name.lower():
                del self.products[i]
                return True
        return False