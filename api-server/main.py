from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import routers.authorize as authorize
app.include_router(authorize.router, prefix='/api/private/v1')

@app.get('/')
async def index():
    return {'hello': 'world'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8888, reload=True, debug=True)
