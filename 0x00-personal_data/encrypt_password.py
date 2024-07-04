#!/usr/bin/env python3
"""
encrypt_password.py

Module for hashing passwords securely using bcrypt and validating hashed passwords.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
    - password (str): Password string to hash.

    Returns:
    - bytes: Salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password using bcrypt.

    Args:
    - hashed_password (bytes): Salted, hashed password stored in bytes.
    - password (str): Password string to validate.

    Returns:
    - bool: True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
