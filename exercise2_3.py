class Lunch(object):
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice: ", self.menu, "Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice: ", self.menu, "Price 13.40")
        else:
            print("Error in menu")

Paul = Lunch("menu 1")
print(Paul.menu_price())
