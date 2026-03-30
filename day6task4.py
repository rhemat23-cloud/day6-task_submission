class User:
    def register(self):
        """Simulate user registration."""
        print("registered")
        return self  # Enable method chaining

    def login(self):
        """Simulate user login."""
        print("logined")
        return self  # Enable method chaining

    def greet(self):
        """Simulate greeting after login."""
        print("enjoy everyone")
        return self  # Enable method chaining


# Example usage
if __name__ == "__main__":
    user = User()
    user.login().greet().register()

