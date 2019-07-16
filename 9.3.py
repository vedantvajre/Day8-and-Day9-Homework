class User():
    def __init__(self, first_name, last_name, password, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.email = email

    def describe_user(self):
        print("First name: " + self.first_name, 'Last name: ' + self.last_name, 'Password: ' + self.password, 'Username: ' + self.username, 'Email ID: ' + self.email)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + ". Welcome to " + self.username.title() + "'s profile!")


user1 = User('Vedant', 'Vajre', 'coolbeans1234', 'VedantVajre', 'vedantvajre@gmail.com')
print(user1)
user1.describe_user()
user1.greet_user()