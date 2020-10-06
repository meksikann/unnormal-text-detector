from fastapi import FastAPI
from server.api import router



app = FastAPI(title='Sentence check server', version='1')


@app.on_event('startup')
async def init_detector():
    print('Language check initialization started')
    from server.api.endpoints.detect import check_language

    await check_language('text init')
    print('Language check initialization finished')





# app.add_middleware(myMiddleware)
app.include_router(router)

