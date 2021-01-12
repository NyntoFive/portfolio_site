from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

##################
# API experiments
from fastapi import APIRouter
from fastapi import Header, HTTPException

# router =APIRouter
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
async def get_query_token(token: str):
    if x_token != "wizard":
        raise HTTPException(status_code=400, detail="No Wizard token provided")
# #
# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]

# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}

# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("home.html", {"request": request, "id": id})

@app.get("/canvas/")
async def canvas(request: Request):
    return templates.TemplateResponse("canvasPage.html",{"request": request, "id": id})
@app.get("/c/")
async def can(request: Request):
    return templates.TemplateResponse("home.html",{"request": request, "id": id})
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, "id": id})

