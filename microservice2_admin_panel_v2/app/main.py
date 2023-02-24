from fastapi import FastAPI, Request
from sqladmin import Admin, ModelView
from app.api.db.base import engine
from app.api.db.models import Auction, User, Item, LotsItemsRelation, Lots
from app.auth_admin import authentication_backend

app = FastAPI()
# admin = Admin(app, engine)
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)


class AuctionAdmin(ModelView, model=Auction):
    column_list = ["id", "title", "description", "place", "date"]

    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class UserAdmin(ModelView, model=User):
    column_list = ["id", "full_name"]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class ItemAdmin(ModelView, model=Item):
    column_list = ["id", "name", "description", "user_id"]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class LotsAdmin(ModelView, model=Lots):
    column_list = ["id", "start_time", "last_price", "is_closed",
                   "auction_id", "seller_id", "new_owner_id"]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


admin.add_view(AuctionAdmin)
admin.add_view(UserAdmin)
admin.add_view(ItemAdmin)
admin.add_view(LotsAdmin)
