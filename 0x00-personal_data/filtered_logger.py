#!/usr/bin/env python3
"""
filtered_logger.py
"""

import logging
import re
from typing import List

# Define filter_datum directly in this file
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

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
