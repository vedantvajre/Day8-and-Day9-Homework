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


class Admin(User):
    def __init__(self, first_name, last_name, password, username, email):
        super().__init__(first_name, last_name, password, username, email)

        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("")


user1 = Admin('Vedant', 'Vajre', 'coolbeans1234', 'VedantVajre', 'vedantvajre@gmail.com')
user1.describe_user()

user1.privileges.show_privileges()

print("\nAdding privileges:")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
user1.privileges.privileges = eric_privileges
user1.privileges.show_privileges()