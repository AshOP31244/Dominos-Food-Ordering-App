import sqlite3

menu = {
    1: ("Margherita Pizza", 99),
    2: ("Cheese n Corn Pizza", 169),
    3: ("Chicken Burger", 179),
    4: ("Veg Burger", 149),
    5: ("Choco Lava Cake", 139),
    6: ("Paneer Pizza", 199)
}

class DominosApp:
    def __init__(self):
        self.conn = sqlite3.connect("dominos.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        self.conn.commit()
        self.cart = []

    def signup(self):
        print("\n--- Sign Up ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        self.conn.commit()
        print("Account created successfully!\n")

    def login(self):
        print("\n--- Log In ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = self.cursor.fetchone()
        if result:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials!\n")
            return False

    def show_menu(self):
        print("\n--- Menu ---")
        for number in menu:
            item = menu[number]
            print("{}. {} - Rs.{}".format(number, item[0], item[1]))

    def take_order(self):
        self.show_menu()
        while True:
            choice = input("Enter item number to add to cart (or 'done' to finish): ")
            if choice.lower() == "done":
                break
            if choice.isdigit():
                number = int(choice)
                if number in menu:
                    self.cart.append(menu[number])
                    print("{} added to cart.".format(menu[number][0]))

    def show_cart(self):
        print("\n--- Your Cart ---")
        total = 0
        for item in self.cart:
            print("{} - Rs.{}".format(item[0], item[1]))
            total += item[1]
        print("Total Bill: Rs.{}".format(total))

# Run directly (no __name__ check)
app = DominosApp()
while True:
    action = input("Choose: (1) Sign Up (2) Log In (3) Exit: ")
    if action == "1":
        app.signup()
    elif action == "2":
        if app.login():
            app.take_order()
            app.show_cart()
    elif action == "3":
        print("Thank you for visiting!")
        break
