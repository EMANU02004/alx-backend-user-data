#!/usr/bin/env python3
""" 0x05. Personal data
"""

import re
import os
import mysql.connector
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Replacing """
    for entry in fields:
        message = re.sub(rf"{entry}=(.*?)\{separator}",
                         f'{entry}={redaction}{separator}', message)
    return message


