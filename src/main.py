from fastapi import FastAPI
from web import explorer, creature, auth, user

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(auth.router)
app.include_router(user.router)


@app.get('/')
def top():
    return "top here"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
