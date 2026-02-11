from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 3200, 6))
manager.add_product(Product("Tv", 40, 10))
manager.add_product(Product("Tastatura", 60, 7))

print("Ukupna vrednost inventara:", manager.total_inventory_value())

from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []           # lista tuple-a: (Product, količina)

    def add_to_cart(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            return
        # Proveri da li već postoji → ako da, samo povećaj količinu
        for item in self.cart_items:
            if item[0].name == product.name:
                item[1] += quantity  # item je tuple → ne može direktno, pa ćemo koristiti listu
                return
        self.cart_items.append([product, quantity])   # lista umesto tuple-a da bi bilo mutable

    def calculate_total(self) -> float:
        return sum(item[0].price * item[1] for item in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("Sadržaj korpe:")
        for item in self.cart_items:
            p, q = item
            print(f"{p.name} x {q}  →  {p.price * q:.2f} €")
        print(f"Ukupno za naplatu: {self.calculate_total():.2f} €")