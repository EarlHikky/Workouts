import fastapi

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/home")
async def root():
    return FileResponse("index.html")
    # return {"message": "Hello World"}


@app.get('/test')
def test():
    return fastapi.Response('Hello', status_code=200, media_type='application/json')
