from fastapi import APIRouter, Request, Body
from src.service import game
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/game")


template_obj = Jinja2Templates(directory='templates', )


@router.get("")
def game_start(request: Request):
    name = game.get_word()
    return template_obj.TemplateResponse("game.html",
                                         {"request": request,
                                          "word": name})


@router.post("")
async def game_step(word: str = Body(), guess: str = Body()) -> str:
    return game.get_score(word, guess)
