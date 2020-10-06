from pytictoc import TicToc
import language_tool_python
from fastapi import APIRouter
from pydantic import BaseModel

# request body class
class DetectRequest(BaseModel):
    text: str

timer = TicToc()
tool = language_tool_python.LanguageTool('en-US')
detect_router = APIRouter()


def detect_errors(text):
    return tool.check(text)


@detect_router.post('/language_check')
async def check_language(item: DetectRequest):
    text = item.text

    timer.tic()
    matches = detect_errors(text)
    timer.toc('Text check took:')

    for match in matches:
        print(match.ruleId)

    return matches
