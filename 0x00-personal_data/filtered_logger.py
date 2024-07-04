#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re


def filter_datum(fields, redaction, message, separator):
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
    return re.sub(
        r'([^{}=;]+)=([^{}=;]*)'.format(separator, separator),
        lambda match: match.group(1) + '=' + redaction if match.group(1) in fields else match.group(0),
        message
    )
