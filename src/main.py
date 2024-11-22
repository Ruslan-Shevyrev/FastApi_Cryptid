from fastapi import FastAPI, Form
from web import explorer, creature, auth, user, files, game
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

top = Path(__file__).resolve().parent


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(files.router)
app.include_router(game.router)

app.mount("/static", StaticFiles(directory='static', html=True), name="free")


@app.get('/')
def top():
    return "top here"


@app.post('/who')
def greet(name: str = Form()):
    return f'Hello {name}'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
