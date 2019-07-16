class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = str(number_served)

    def describe_restaurant(self):
        print("\nRestaurant Name: " + self.restaurant_name)
        print("\nCuisine Type: " + self.cuisine_type)
        print('\nNumber of customers served: ' + self.number_served)

    def open_restaurant(self):
        print("\nThe Restaurant is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, more_served):
        self.number_served += more_served


restaurant = Restaurant("Saffron", 'Cuisine', 9)
restaurant.describe_restaurant()
print(restaurant)
restaurant.number_served = 430
print(str(restaurant.number_served))
restaurant.set_number_served(50)
print(str(restaurant.set_number_served))
restaurant.increment_number_served(25)
print(str(restaurant.increment_number_served))
