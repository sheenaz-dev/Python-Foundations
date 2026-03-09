# --- THE MENU CLASS ---
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

# --- THE FRANCHISE CLASS ---
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available.append(menu)
        return available

# --- INSTANTIATION ---
brunch = Menu("brunch", {'pancakes': 7.5, 'coffee': 1.5}, 11, 16)
early_bird = Menu("early_bird", {'salumeria': 8.0, 'pizza': 9.0}, 15, 18)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird])

# --- TESTING ---
print(brunch) # Test __repr__
print(f"Brunch Total: ${brunch.calculate_bill(['pancakes', 'coffee'])}")
print(f"Available at 12pm: {flagship_store.available_menus(12)}")