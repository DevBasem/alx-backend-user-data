#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth

import base64

from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication

        Args:
            authorization_header (str): The Authorization
            header from the request

        Returns:
            str: The Base64 part of the Authorization
            header, or None if invalid
        """
        if (
            authorization_header is None or
            not isinstance(authorization_header, str)
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes a Base64 encoded string

        Args:
            base64_authorization_header (str): The Base64
            encoded string

        Returns:
            str: The decoded string in UTF-8, or None
            if decoding fails
        """
        if (
            base64_authorization_header is None or
            not isinstance(base64_authorization_header, str)
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user credentials (email and password) from
        a decoded Base64 authorization header

        Args:
            decoded_base64_authorization_header (str): The decoded
            Base64 authorization header

        Returns:
            tuple: A tuple containing user email and password,
            or (None, None) if invalid
        """
        if (
            decoded_base64_authorization_header is None or
            not isinstance(decoded_base64_authorization_header, str) or
            ':' not in decoded_base64_authorization_header
        ):
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """
        Returns the User instance based on email and password

        Args:
            user_email (str): User's email
            user_pwd (str): User's password

        Returns:
            User: The User instance if credentials are valid,
            None otherwise
        """
        if (
            user_email is None or not isinstance(user_email, str) or
            user_pwd is None or not isinstance(user_pwd, str)
        ):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
