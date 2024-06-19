"""
Web API for the Boggle game

pip install fastapi uvicorn
--> uvicorn --reload web_app:app
--> python -m uvicorn --reload web_app:app
--> go to http://127.0.0.1:8000 in your browser
"""
import socket

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from boggle import start_game, guess_word
import boggle  # reference to the module boggle

from model import CheckWordRequest, CheckWordResponse

app = FastAPI()
jinja_env = Environment(loader=FileSystemLoader("templates"))


@app.get("/boggle/view")
async def view():
    message = "Let's play Boggle"
    template = jinja_env.get_template("boggle.html")
    return HTMLResponse(
        template.render(
            message=message,
            table=boggle.table,
            guesses=boggle.guesses,
            ip_address=get_ip(),
        )
    )


@app.post("/boggle/check_word")
async def check(request: CheckWordRequest) -> CheckWordResponse:
    return guess_word(request)


@app.get("/boggle/{xsize}/{ysize}")
async def new_game_custom_size(xsize: int, ysize: int):
    return start_game(xsize=xsize, ysize=ysize)


@app.get("/boggle")
async def new_game():
    return start_game(xsize=4, ysize=4)


@app.get("/")
async def hello():
    return {"message": "Hello World"}


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(("10.254.254.254", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP
