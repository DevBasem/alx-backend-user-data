#!/usr/bin/env python3
"""
Auth module for API authentication
"""

from typing import List

class Auth:
    """Template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if a path requires authentication based on excluded paths.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths to exclude from authentication.
                                        Paths may include * as a wildcard at the end.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                prefix = excluded_path.rstrip('*')
                if path.startswith(prefix):
                    return False
            elif path == excluded_path:
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
