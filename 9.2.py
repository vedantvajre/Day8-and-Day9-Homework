class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant Name: " + self.restaurant_name)
        print("\nCuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("\nThe Restaurant is open!")


instance1 = Restaurant('Pizza Hut', 'Pizza')
print(instance1)
instance1.describe_restaurant()
instance2 = Restaurant('Olive Garden', 'Italian')
print(instance2)
instance2.describe_restaurant()
instance3 = Restaurant('Mai Thai', 'Chinese')
print(instance3)
instance3.describe_restaurant()