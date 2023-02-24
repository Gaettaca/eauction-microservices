from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.api.db.models import Auction
from app.api.db.queries import *
from app.api.schemas import *

from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

templates = Jinja2Templates(directory="app/templates")

auctions = APIRouter()


@auctions.get('/')
async def index(request: Request):
    auctions = await get_all_auctions()
    # return {'Auctions': result}
    return templates.TemplateResponse("general_pages/homepage_auctions.html",
                                      {"request": request, "auctions": auctions})


@auctions.get('/detail/{auction_id}')
async def exact_auction(auction_id: int, request: Request):
    auction = await get_auction_by_id(auction_id)
    return templates.TemplateResponse("auctions/detail.html",
                                      {"request": request, "auction": auction})
