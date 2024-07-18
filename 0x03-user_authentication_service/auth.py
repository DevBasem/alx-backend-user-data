#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if email does not exist,
        otherwise raise ValueError
        """
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password
            hashed_password = self._hash_password(password)
            # Add the user to the database
            user = self._db.add_user(email, hashed_password)
            return user

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password using bcrypt.hashpw
        """
        import bcrypt
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
