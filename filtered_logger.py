#!/usr/bin/env python3
""" 0x05. Personal data
"""

import re
import os
import mysql.connector
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")

