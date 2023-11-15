from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already taken")
        if not valid_username(username):
            raise UserInputError(
                "Username must be at least three letters long and contain only letters")
        if not valid_password(password):
            raise UserInputError(
                "Password must be at least eight symbols long and contain not only letters")


def valid_username(s):
    return bool(re.fullmatch(r'[a-z]{3,}', s))


def valid_password(s):
    return bool(re.fullmatch(r'(?=.{8,})(?!^[a-zA-Z]*$).+', s))
