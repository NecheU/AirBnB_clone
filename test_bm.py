#!/usr/bin/python3
"""Doc
"""
from models.base_model import *
from models.base_model import BaseModel


class BaseModel(BaseModel):
    """Doc
    """

    def __init__(self, *args, **kwargs):
        """Doc
        """
        if args is not None and len(args) > 0:
            pass
        else:
            BaseModel.__init__(self, args, kwargs)
