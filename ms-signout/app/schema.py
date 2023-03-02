import logging
import re
from typing import Optional, TypeVar

from fastapi import HTTPException
from pydantic import BaseModel, validator
from sqlalchemy import false

T = TypeVar('T')

# get root logger
logger = logging.getLogger(__name__)


class LogoutSchema(BaseModel):
    username: str


class DetailSchema(BaseModel):
    status: str
    message: str
    result: Optional[T] = None


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
