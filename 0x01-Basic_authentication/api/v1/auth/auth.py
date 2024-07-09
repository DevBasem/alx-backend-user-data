#!/usr/bin/env python3
"""
Auth module for API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if a path requires authentication

        Args:
            path (str): The path to check

        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the request

        Args:
            request (flask.Request): The Flask request object

        Returns:
            str: The authorization header, or None if not present
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user from the request

        Args:
            request (flask.Request): The Flask request object

        Returns:
            TypeVar('User'): None since no user is identified (placeholder)
        """
        return None
