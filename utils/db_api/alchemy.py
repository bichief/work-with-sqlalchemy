from data import config
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey, ForeignKeyConstraint, \
    PrimaryKeyConstraint, UniqueConstraint

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer()),
              Column('name', String(200), nullable=False),
              Column('username', String(200), nullable=False),
              PrimaryKeyConstraint('id'),
              UniqueConstraint('id')
              )

balance = Table('balance', metadata,
                Column('amount', Integer()),
                Column('user_id', ForeignKey('users.id'))
                )

goods = Table('goods', metadata,
              Column('id', Integer(), unique=True),
              Column('name', String(200), nullable=False, unique=True),
              Column('description', String(255), nullable=False),
              Column('price', Integer(), unique=True),
              PrimaryKeyConstraint('id', 'name', 'price'),
              )

picture = Table('picture', metadata,
                Column('id', Integer()),
                Column('url', String(255)),
                Column('goods_id', ForeignKey('goods.id')),
                )

cart = Table('cart', metadata,
             Column('user_id', Integer(), ForeignKey('users.id')),
             Column('goods_name', String(200), ForeignKey('goods.name'), nullable=False),
             Column('goods_price', Integer(), ForeignKey('goods.price'), nullable=False),
             Column('goods_id', Integer(), ForeignKey('goods.id'), nullable=False),
             # ForeignKeyConstraint()
             )

engine = create_engine(
    f'{config.DATABASE}+{config.DRIVER}://{config.USERNAME}:{config.PASSWORD}@{config.HOST}/{config.NAME}')

metadata.create_all(engine)
