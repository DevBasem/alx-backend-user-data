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
    pattern = r'([^{}=;]+)=([^{}=;]*)'.format(separator, separator)

    def obfuscate_field(match):
        """
        Helper function to obfuscate a matched field.
        """
        field_name = match.group(1)
        field_value = match.group(2)

        if field_name in fields:
            return field_name + '=' + redaction
        else:
            return field_name + '=' + field_value

    return separator.join(
        [obfuscate_field(m) for m in re.finditer(pattern, message)]
    )
