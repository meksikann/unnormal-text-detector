"""
given a text batch
detect if each ENG sentence is unnormal

"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


detect_router = APIRouter()


@detect_router.get('/language_check')
async def check_language():

    return 'Text is ok'
