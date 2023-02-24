from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.auctions import auctions

app = FastAPI(openapi_url="/api/v1/auctions/openapi.json", docs_url="/api/v1/auctions/docs")
app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})


app.include_router(auctions, prefix='/api/v1/auctions', tags=['auctions'])
