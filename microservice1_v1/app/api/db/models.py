
from sqlalchemy.orm import declarative_base
import sqlalchemy as sa

Base = declarative_base()


class Auction(Base):
    __tablename__ = "auction"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    place = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.Date)

    def __repr__(self):
        return '<Auction (id={0.id}) (place="{0.place}") (date="{0.date}")>'.format(self)


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.Text, nullable=False)

    def __repr__(self):
        return '<User (id={0.id}) (fname="{0.full_name}")>'.format(self)


class Item(Base):
    __tablename__ = "goods"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'), nullable=True)

    def __repr__(self):
        return '<Item (id={0.id}) (name="{0.name}") (dscrp="{0.description}") (user_id={0.user_id})>'.format(self)


class LotsItemsRelation(Base):
    __tablename__ = "lots_goods_relation"

    lot_id = sa.Column(sa.Integer, sa.ForeignKey('lots.id', ondelete='CASCADE'), primary_key=True)
    item_id = sa.Column('good_id', sa.Integer, sa.ForeignKey('goods.id', ondelete='CASCADE'), primary_key=True)

    def __repr__(self):
        return "<Lots_goods_relation (lot_id={0.lot_id}) (item_id={0.item_id})>".format(self)


class Lots(Base):
    __tablename__ = "lots"

    id = sa.Column(sa.Integer, primary_key=True)
    start_time = sa.Column(sa.Time, nullable=False)
    last_price = sa.Column(sa.Integer, nullable=False)  # Проверить!!!
    is_closed = sa.Column(sa.Boolean, default=False)
    auction_id = sa.Column(sa.Integer, sa.ForeignKey('auction.id', ondelete='CASCADE'), nullable=False)
    seller_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    new_owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)

    def __repr__(self):
        return '<Lots (id={0.id})>'.format(self)
