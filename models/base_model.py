#!/usr/bin/python3
""" class BaseModel that defines
    all common attributes/methods
    for other classes:
"""
import uuid
from datetime import date


class BaseModel:
    """
    """
    id = ""

    def __init__(self):
        self.id = uuid.uuid4().bytes


if __name__ == "__main__":
    return
