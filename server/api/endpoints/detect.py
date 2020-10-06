from pytictoc import TicToc
import language_tool_python
from fastapi import APIRouter

# from pydantic import BaseModel
# from typing import List

timer = TicToc()
tool = language_tool_python.LanguageTool('en-US')
detect_router = APIRouter()

good_text = '[CWD-120] I was working on bug fixing due to the ticketяя created'


@detect_router.get('/language_check/{text}')
async def check_language(text):
    timer.tic()
    matches = tool.check(text)
    timer.toc('Text check took:')

    feedback = ''

    for match in matches:
        print(match.ruleId)
        feedback += "" + match.ruleId

    return feedback
