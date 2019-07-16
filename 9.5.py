class User():

    def __init__(self, first_name, last_name, password, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name, 'Last name: ' + self.last_name, 'Password: ' + self.password,
              'Username: ' + self.username, 'Email ID: ' + self.email)

    def greet_user(self):
        print(
            "Hello " + self.first_name.title() + " " + self.last_name.title() + ". Welcome to " + self.username.title() + "'s profile!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


Vedant = User('Vedant', 'Vajre', 'coolbeans1234', 'VedantVajre', 'vedantvajre@gmail.com')
Vedant.describe_user()
Vedant.greet_user()

print("\nMaking 5 login attempts:")
Vedant.increment_login_attempts()
Vedant.increment_login_attempts()
Vedant.increment_login_attempts()
Vedant.increment_login_attempts()
Vedant.increment_login_attempts()
print("  Login attempts: " + str(Vedant.login_attempts))

print("Resetting login attempts:")
Vedant.reset_login_attempts()
print("  Login attempts: " + str(Vedant.login_attempts))