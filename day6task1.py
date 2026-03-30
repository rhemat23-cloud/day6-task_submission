class User:
    def __init__(self):
        # Private variables (name mangling with __)
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name: str, pwd: str):
        """
        Sets the username and password with basic validation.
        """
        if not isinstance(user_name, str) or not isinstance(pwd, str):
            raise TypeError("Username and password must be strings.")
        if not user_name.strip():
            raise ValueError("Username cannot be empty.")
        if len(pwd) < 4:
            raise ValueError("Password must be at least 4 characters long.")

        self.__user_name = user_name.strip()
        self.__pwd = pwd

    def get_user(self) -> str:
        """
        Returns only the username (password is hidden).
        """
        return self.__user_name

    def register(self):
        """
        Prints the registered username.
        """
        if self.__user_name is None:
            print("No user registered yet.")
        else:
            print(f"User '{self.__user_name}' registered successfully.")

    def login(self, user_name: str, pwd: str):
        """
        Simulates a login process.
        """
        if self.__user_name is None:
            print("No user registered. Please register first.")
            return

        if user_name == self.__user_name and pwd == self.__pwd:
            print(f"Login successful. Welcome, {self.__user_name}!")
        else:
            print("Login failed. Invalid username or password.")


# Example usage
if __name__ == "__main__":
    user = User()

    try:
        user.set_user("raja", "pswd123")
        user.register()
        print("Stored username (via getter):", user.get_user())

        # Attempt login
        user.login("raja", "pswd123")  # Correct credentials
        user.login("raja", "wrong")    # Wrong password
    except (TypeError, ValueError) as e:
        print("Error:", e)
