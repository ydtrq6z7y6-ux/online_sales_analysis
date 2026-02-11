from product import Product
from product_manager import ProductManager

# Inicijalizacija managera i dodavanje proizvoda
manager = ProductManager()
manager.add_product(Product("Laptop", 3200, 6))
manager.add_product(Product("Tv", 40, 10))
manager.add_product(Product("Tastatura", 60, 7))

print(f"Ukupna vrednost inventara: {manager.total_inventory_value()}")

class Cart:
    def __init__(self):
        # Koristimo listu listi [Product, kolicina] da bi bila mutable (promjenjiva)
        self.cart_items = [] 

    def add_to_cart(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            return
        
        # Provjera postoji li već isti proizvod u košarici
        for item in self.cart_items:
            if item[0].name == product.name:
                item[1] += quantity  # Povećavamo količinu (ovo radi jer je item lista)
                return
        
        # Ako proizvod ne postoji, dodajemo ga kao novu listu unutar košarice
        self.cart_items.append([product, quantity])

    def calculate_total(self) -> float:
        return sum(item[0].price * item[1] for item in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        
        print("\nSadržaj korpe:")
        for item in self.cart_items:
            p, q = item
            print(f"{p.name} x {q} -> {p.price * q:.2f} €")
        
        print(f"Ukupno za naplatu: {self.calculate_total():.2f} €")

# --- TESTNI DIO (ovo možeš obrisati kasnije) ---
if __name__ == "__main__":
    moja_korpa = Cart()
    
    # Uzimamo proizvode iz managera za test
    p1 = Product("Laptop", 3200, 6)
    p2 = Product("Tastatura", 60, 7)
    
    moja_korpa.add_to_cart(p1, 1)
    moja_korpa.add_to_cart(p2, 2)
    moja_korpa.add_to_cart(p1, 1)  # Dodajemo opet isti proizvod da provjerimo zbrajanje
    
    moja_korpa.display_cart()