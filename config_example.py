"""
Example configuration file.

Copy this file to config.py and adjust the values.
"""

from pathlib import Path

# ==================================================
# Project paths
# ==================================================

#---- Paths ------------------
BASE_DIR = Path(__file__).resolve().parent
LOG_FILENAME = "example.log"
QUOTE_FILENAME = "example.json"

# Convert Path to str for compatibility with older Python / libraries
LOGGING = BASE_DIR / LOG_FILENAME
QUOTES  = BASE_DIR / QUOTE_FILENAME

# ---- SMTP ----------------
SMTP_HOST = "mail.example.com"
SMTP_USER = "John.Doe@example.com"
SMTP_PORT = 587
SMTP_PASSWORD = "***********"

# ---- Mail ----------------
FROM_ADDR = "noreply@example.com"
TO_ADDR = "John.Doe@example.com"
SUBJECT = "Monday's Motivational Quote"
