from fastapi import FastAPI
from web import explorer, creature, auth

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(auth.router)

@app.get('/')
def top():
    return "top here"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echo {thing}"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
