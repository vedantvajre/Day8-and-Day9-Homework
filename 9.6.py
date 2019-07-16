class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant Name: " + self.restaurant_name)
        print("\nCuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("\nThe Restaurant is open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand("Vedant's Restaurant")
big_one.flavors = ['Vanilla', 'Strawberry', 'Chocolate']

big_one.describe_restaurant()
big_one.show_flavors()