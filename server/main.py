from fastapi import FastAPI
from server.api import router

app = FastAPI(title='Sentence check server', version='1')

# app.add_middleware(myMiddleware)
app.include_router(router)

