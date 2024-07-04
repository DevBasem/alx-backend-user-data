#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specific fields in a log message.

    Args:
    - fields (list of str): List of field names to obfuscate.
    - redaction (str): String used to replace obfuscated fields.
    - message (str): Log message containing fields to obfuscate.
    - separator (str): Separator character used to separate fields
    in the message.

    Returns:
    - str: Log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
