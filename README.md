🍕 Dominos Food Ordering App (Python + SQLite)
📌 Project Overview

This is a command-line food ordering system built in Python using SQLite for data storage.
Users can sign up, log in, browse the menu, add items to their cart, and view the total bill — all from the terminal.
It’s a beginner-friendly project to understand database integration, OOP concepts, and user authentication.

⚙️ Features

✅ User Signup and Login (stored securely in SQLite database)
✅ Interactive text-based menu
✅ Add multiple food items to cart
✅ Automatic bill calculation
✅ Persistent data storage using SQLite
✅ Simple and beginner-friendly code structure

🧠 Tech Stack

Language: Python

Database: SQLite3 (local file-based database)

🗂️ Project Structure
DominosApp/
│
├── dominos.py        # Main Python file (your app)
├── dominos.db        # SQLite database (auto-created)
└── README.md         # Project documentation

🚀 How to Run

Clone the repository

git clone https://github.com/<your-username>/DominosApp.git
cd DominosApp


Run the Python file

python dominos.py


Use the App

Choose (1) to create a new account

Choose (2) to log in

Browse the menu and add items to your cart

View your final bill

🧾 Example Run
Choose: (1) Sign Up (2) Log In (3) Exit: 1
--- Sign Up ---
Enter username: ashwaz
Enter password: 1234
Account created successfully!

Choose: (1) Sign Up (2) Log In (3) Exit: 2
--- Log In ---
Enter username: ashwaz
Enter password: 1234
Login successful!

--- Menu ---
1. Margherita Pizza - Rs.99
2. Cheese n Corn Pizza - Rs.169
...

Enter item number to add to cart (or 'done' to finish): 1
Margherita Pizza added to cart.
Enter item number to add to cart (or 'done' to finish): done

--- Your Cart ---
Margherita Pizza - Rs.99
Total Bill: Rs.99

🧑‍💻 Author

Ashwaz Poojary
📧 ashwajpoojary2@gmail.com
