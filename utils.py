# utils.py
"""Utility functions shared across different tool modules."""

import datetime
from typing import Dict, Any
from . import config  # Use relative import


def get_current_date() -> str:
    """Returns the current date as a string in ISO format."""
    return datetime.date.today().isoformat()


def create_error_response(message: str) -> Dict[str, str]:
    """Creates a standardized error response dictionary."""
    return {"status": config.STATUS_ERROR, "error_message": message}


def generate_pseudo_unique_id(prefix: str, *args: Any) -> str:
    """
    Generates a pseudo-unique ID based on a prefix and input arguments.
    Note: hash() is NOT suitable for production uniqueness guarantees.
    Replace with a robust ID generation method in a real application.
    """
    combined_input = "".join(map(str, args))
    # Simple hash-based generation for demonstration
    unique_part = hash(combined_input) % 1000000
    return f"{prefix}{unique_part:06d}"
