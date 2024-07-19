#!/usr/bin/env python3
"""
Auth module
"""

import logging
from typing import Union
from uuid import uuid4

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User

logging.disable(logging.WARNING)


def _hash_password(password: str) -> bytes:
    """Hashes a password and returns bytes.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a uuid.

    Returns:
        str: string representation of a new UUID.
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with the given email and password.

        Args:
            email (str): The email of the new user.
            password (str): The password of the new user.

        Returns:
            User: A User object representing the newly created user.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            # Search for the user by email
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        # If not, hash the password with _hash_password
        hashed_password = _hash_password(password)
        # Save the user to the database using self._db
        user = self._db.add_user(email, hashed_password)
        # Return the User object
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password to check.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)
            # Check if the provided password matches the stored hashed password
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """Creates a session ID for the user with the given email.

        Args:
            email (str): The email of the user.

        Returns:
            Union[str, None]: The session ID as a string if the
            user is found, None otherwise.
        """
        try:
            # Retrieve the user by email
            user = self._db.find_user_by(email=email)

            # Generate a new session ID
            session_id = _generate_uuid()

            # Update the user's session_id in the database
            self._db.update_user(user.id, session_id=session_id)

            # Return the session ID
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Finds and returns a user based on a session ID.

        Args:
            session_id (str): The session ID of the user.

        Returns:
            Union[User, None]: The user object if found, None otherwise.
        """
        if session_id is None:
            return None

        try:
            # Retrieve the user by session ID
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session ID for the user with the given user ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            None
        """
        try:
            # Update the user's session_id to None
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass
