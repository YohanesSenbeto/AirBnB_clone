#!/usr/bin/env python3
"""
The 'user' module presents the User class for our  application.
"""

from base_model import BaseModel


class User(BaseModel):
    """Represents a user in the application."""

    email = ""
    """str: The email address of the user."""

    password = ""
    """str: The password of the user."""

    first_name = ""
    """str: The first name of the user."""

    last_name = ""
    """str: The last name of the user."""
