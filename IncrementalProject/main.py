from models.product import Product
from registry.registry import ProductRegistry

laptop = Product("Laptop", 80000, 15)
mouse = Product("Wireless Mouse", 1500, 50)
keyboard = Product("Mechanical Keyboard", 5000, 50)

print("\nProduct Details")
print("-" * 40)

laptop.display_details()
mouse.display_details()
keyboard.display_details()

ProductRegistry.display_registered_products()
