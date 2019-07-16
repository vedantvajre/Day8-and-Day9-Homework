class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nRestaurant Name: " + self.restaurant_name)
        print("\nCuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("\nThe Restaurant is open!")


restaurant = Restaurant("Saffron", "Indian")
print(restaurant)
restaurant.describe_restaurant()
restaurant.open_restaurant()