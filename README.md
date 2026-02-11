online_sales_analysis/
│
├── product.py
├── product_manager.py
├── cart.py
├── main.py
├── .gitignore
├── README.md

Core Components
1. Product (product.py)

Represents a single product in the inventory.

Attributes:

name – product name

price – product price

quantity – available stock quantity

Methods:

Display product information

Update product quantity
2. ProductManager (product_manager.py)

Manages all available products in the system.

Responsibilities:

Add new products

Remove products by name

Display all available products

Calculate total inventory value

This class acts as the inventory management layer of the system.

3. Cart (cart.py)

Represents a customer shopping cart.

Attribute:

cart_items – list of selected products

Methods:

Add products to cart

Display cart contents

Calculate total amount for checkout

4. Main Application (main.py)

The entry point of the application.

Responsibilities include:

Creating product instances

Managing inventory through ProductManager

Simulating customer cart functionality

Displaying checkout total
Features Implemented Through Git Workflow

Initial project setup and commit

Feature branch creation (add-product-removal)

Implementation of product removal functionality

Feature branch creation (add-cart-functionality)

Implementation of shopping cart system

Merge conflict resolution

Proper .gitignore configuration

Clean commit history with meaningful messages

.gitignore Configuration

The project ignores:

config.json (contains sensitive data such as API keys)

Screenshot files (e.g., *.png, *.jpg)

System-specific files (optional: .DS_Store, __pycache__/, etc.)

This ensures that sensitive and unnecessary files are not tracked or pushed to GitHub.
Features Implemented Through Git Workflow

Initial project setup and commit

Feature branch creation (add-product-removal)

Implementation of product removal functionality

Feature branch creation (add-cart-functionality)

Implementation of shopping cart system

Merge conflict resolution

Proper .gitignore configuration

Clean commit history with meaningful messages

.gitignore Configuration

The project ignores:

config.json (contains sensitive data such as API keys)

Screenshot files (e.g., *.png, *.jpg)

System-specific files (optional: .DS_Store, __pycache__/, etc.)

This ensures that sensitive and unnecessary files are not tracked or pushed to GitHub.

How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/online_sales_analysis.git

2. Navigate to the project folder
cd online_sales_analysis

3. Run the application
python main.py

Technologies Used

Python 3

Git

GitHub

Learning Outcomes

Through this project, the following skills were reinforced:

Writing modular Python code

Applying OOP design principles

Managing branches in Git

Handling merge conflicts

Structuring a professional repository

Author

Tina Rako Saric
GitHub: https://github.com/ydtrq6z7y6-ux