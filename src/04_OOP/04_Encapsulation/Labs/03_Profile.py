class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_long_enough = len(value) >= 8
        is_upper_any = any([p for p in value if p.isupper()])
        is_digit_any = any([p for p in value if p.isdigit()])

        if not(is_long_enough and is_upper_any and is_digit_any):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return (f'You have a profile with username: "{self.username}" '
                f'and password: {"*" * len(self.password)}')


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
